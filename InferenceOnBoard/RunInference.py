import os
import time
import shutil
import numpy as np
import rasterio
import xir
import vart
from vart import Runner
from datetime import datetime

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

def preprocess_image(original_image):
    pad_width = ((0, 0), (1, 0), (1, 0))
    padded_image = np.pad(original_image, pad_width, mode='constant')
    padded_image = np.pad(padded_image, ((0, 0), (0, 2), (0, 2)), mode='constant')
    return padded_image

def get_child_subgraph_dpu(graph):
    assert graph is not None, "'graph' nu ar trebui să fie None."
    root_subgraph = graph.get_root_subgraph()
    assert root_subgraph is not None, "'root_subgraph' ar trebui să fie root."
    subgraphs = root_subgraph.toposort_child_subgraph()
    assert len(subgraphs) != 0, "Nu a fost găsit niciun subgraph."
    for subgraph in subgraphs:
        if subgraph.has_attr("device") and subgraph.get_attr("device").upper() == "DPU":
            return subgraph
    return None

def read_image(image_path):
    attempts = 0
    max_attempts = 30
    
    while attempts < max_attempts:
        try:
            with rasterio.open(image_path) as src:
                image = src.read()
                image = image / 10000
            return image
        except Exception as e:
            if attempts < max_attempts - 1:
                print(f"Imaginea nu a fost complet primită, încercare {attempts + 1}...")
            time.sleep(1)
            attempts += 1
    
    print("Nu s-a reușit citirea imaginii după 10 încercări. Eliminarea imaginii de pe disc.")
    os.remove(image_path)
    return None

def run_inference(model_path, image_path, output_dir):
    print(f"Se analizează {image_path}")

    graph = xir.Graph.deserialize(model_path)
    subgraph = get_child_subgraph_dpu(graph)
    runner = Runner.create_runner(subgraph, "run")

    input_image = read_image(image_path)
    input_image = preprocess_image(input_image)
    input_image = np.expand_dims(np.moveaxis(input_image, 0, -1), axis=0) 

    input_tensors = runner.get_input_tensors()
    output_tensors = runner.get_output_tensors()

    input_data = [np.array(input_image, dtype=np.float32, order='C')]
    output_data = [np.empty(output_tensors[0].dims, dtype=np.float32)]

    start_time = time.time()  # Start timing
    job_id = runner.execute_async(input_data, output_data)
    runner.wait(job_id)
    end_time = time.time()  # End timing

    duration = end_time - start_time
    print(f"Execuția prezicerii a durat: {duration:.2f} secunde")

    output = output_data[0]
    output_labels = np.squeeze(output, axis=0) 
    argmax_channels = np.argmax(output_labels, axis=-1)

    total_pixels = argmax_channels.size
    cloud_pixels = np.count_nonzero((argmax_channels == 1) | (argmax_channels == 3))
    cloud_percentage = (cloud_pixels / total_pixels) * 100

    print(f"Procentul de nori este: {cloud_percentage} %")

    if (cloud_percentage < 70):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        timestamped_dir = os.path.join(output_dir, timestamp)
        timestamped_dir += '_files'
        os.makedirs(timestamped_dir, exist_ok=True)

        output_path = os.path.join(timestamped_dir, f"result.npy")
        np.save(output_path, argmax_channels)
        print(f"Etichetele rezultate au fost salvate în {output_path}")

        shutil.move(image_path, os.path.join(timestamped_dir, 'image.tiff'))
        print(f"Imaginea originală a fost mutată în {timestamped_dir}")
    else:
        os.remove(image_path)

def monitor_and_analyze(unanalized_dir, analized_dir, model_path):
    while True:
        for filename in os.listdir(unanalized_dir):
            if filename.endswith(".tif") or filename.endswith('.tiff'):
                image_path = os.path.join(unanalized_dir, filename)
                output_dir = analized_dir
                try:
                    run_inference(model_path, image_path, output_dir)
                except Exception as e:
                    print(f"A apărut o eroare în timpul procesării {filename}: {e}")
                    continue
                    
        time.sleep(1)

if __name__ == "__main__":
    model_path = "./mobilenetv2_pt/mobilenetv2_pt.xmodel"
    unanalized_dir = "/home/root/unanalized"
    analized_dir = "/home/root/analized"

    print(f"Se monitorizează {unanalized_dir} pentru imagini noi de analizat...")
    monitor_and_analyze(unanalized_dir, analized_dir, model_path)
