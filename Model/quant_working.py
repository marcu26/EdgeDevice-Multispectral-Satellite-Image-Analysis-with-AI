import os
import re
import sys
import time
import random
from pytorch_nndct.apis import torch_quantizer, dump_xmodel
import torch
import torchvision
import torchvision.transforms as transforms
import segmentation_models_pytorch as smp
import numpy as np

from tqdm import tqdm

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")



#quant_mode = modul de cuantizare
#finetune = daca e pe true face si finetune pentru model
#deploy = daca e setat pe true face un deploy pentru model
#batch_size = cat de mare este batch-ul cu care isi face cuantizarea
#subset_len = cate poze sunt in dataset-ul pe care se face evaluarea si finetune-ul

class Parameters:
    def __init__(self, quant_mode, finetune, deploy, batch_size, subset_len):
        self.quant_mode = quant_mode
        self.finetune = finetune
        self.deploy = deploy
        self.batch_size = batch_size
        self.subset_len = subset_len

args = Parameters('test',True,True,1,1)


def load_data(folder='./TestDataSet/', test_shape=(args.subset_len, 512, 512)):

    images = []

    for i in range(13):
        if i < 8:
            file = "L1C_B" + str(i + 1) + ".dat"
            image = np.memmap(os.path.join(folder, file), dtype='int16', mode='r', shape=test_shape)
        elif i == 8:
            file = 'L1C_B8A.dat'
            image = np.memmap(os.path.join(folder, file), dtype='int16', mode='r', shape=test_shape)
        else:
            file = "L1C_B" + str(i) + ".dat"
            image = np.memmap(os.path.join(folder, file), dtype='int16', mode='r', shape=test_shape)

        images.append(image / 10000)

    images = np.stack(images, axis=1)
    images_tensor = torch.from_numpy(images).float()

    y = np.memmap('./TestDataSet/LABEL_manual_hq.dat', dtype='int8', mode='r', shape=test_shape)

    return images_tensor, y


def evaluate(model, y, image_tensor):
    model.eval()
    model = model.to(device)
    matching_pixels = 0

    with torch.no_grad():
        outputs = model(image_tensor)
        total_pixels = np.prod(y.shape)
        output_np = outputs.cpu().numpy()  
        predictions = np.argmax(output_np, axis=1)
        matching_pixels = np.sum(predictions == y)

        # Acuratete
        accuracy = matching_pixels / total_pixels

        # IoU
        intersection = np.logical_and(predictions, y)
        union = np.logical_or(predictions, y)
        iou = np.sum(intersection) / np.sum(union)

        # Scorul F1
        TP = np.sum(predictions & y)
        precision = TP / (np.sum(predictions) + 1e-7)
        recall = TP / (np.sum(y) + 1e-7)
        f1_score = 2 * (precision * recall) / (precision + recall + 1e-7)

        # Distanța medie euclidiană
        euclidean_distance = np.linalg.norm(predictions - y)

    return accuracy, iou, f1_score, euclidean_distance

def quantization(file_path=''): 

  quant_mode = args.quant_mode
  finetune = args.finetune
  deploy = args.deploy
  batch_size = args.batch_size
  subset_len = args.subset_len
  if quant_mode != 'test' and deploy:
    deploy = False
    print(r'Warning: Exporting xmodel needs to be done in quantization test mode, turn off it in this running!')
  if deploy and (batch_size != 1 or subset_len != 1):
    print(r'Warning: Exporting xmodel needs batch size to be 1 and only 1 iteration of inference, change them automatically!')
    batch_size = 1
    subset_len = 1

  model = smp.Unet(encoder_name="mobilenet_v2", encoder_weights=None, in_channels=13, classes=4)
  checkpoint = torch.load(file_path, map_location=torch.device(device))
  model.load_state_dict(checkpoint)

  input = torch.randn([batch_size, 13, 512, 512])
  if quant_mode == 'float':
    quant_model = model
  else:
    ## new api
    ####################################################################################
    quantizer = torch_quantizer(quant_mode, model, (input), device=device)
    quant_model = quantizer.quant_model
    #####################################################################################

  # fast finetune model or load finetuned parameter before test
  if finetune == True:
      images, labels = load_data(test_shape=(1,512,512))
      if quant_mode == 'calib':
        quantizer.fast_finetune(evaluate, (quant_model,  labels, images))
      elif quant_mode == 'test':
        quantizer.load_ft_param()


  images, labels = load_data(test_shape=(1,512,512))

  accuracy, iou, f1_score, euclidean_distance = evaluate(quant_model, labels, images)
  print('accuracy: ', accuracy)
  print('accuracy:', accuracy)
  print('IOU:', iou)
  print('F1 Score:', f1_score)
  print('Euclidean Distance:', euclidean_distance)

  # handle quantization result
  if quant_mode == 'calib':
    quantizer.export_quant_config()
  if deploy:
    quantizer.export_xmodel(output_dir = '.',deploy_check=False)
    print("deployed")


if __name__ == '__main__':
  model_name = 'mobilenet_v2'
  file_path = './mobilenet_v2.pth'

  feature_test = ' float model evaluation'
  if args.quant_mode != 'float':
    feature_test = ' quantization'
    # force to merge BN with CONV for better quantization accuracy
    args.optimize = 1
    feature_test += ' with optimization'
  else:
    feature_test = ' float model evaluation'
  title = model_name + feature_test

  print("-------- Start {} test ".format(model_name))

  # calibration or evaluation
  quantization(file_path=file_path)

  print("-------- End of {} test ".format(model_name))