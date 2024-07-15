# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class Unet(torch.nn.Module):
    def __init__(self):
        super(Unet, self).__init__()
        self.module_0 = py_nndct.nn.Input() #Unet::input_0
        self.module_1 = py_nndct.nn.Conv2d(in_channels=13, out_channels=32, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/ConvNormActivation[features]/ConvNormActivation[0]/Conv2d[0]/input.1
        self.module_2 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/ConvNormActivation[features]/ConvNormActivation[0]/ReLU[2]/input.5
        self.module_3 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=32, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[1]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.7
        self.module_4 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[1]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.11
        self.module_5 = py_nndct.nn.Conv2d(in_channels=32, out_channels=16, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[1]/Sequential[conv]/Conv2d[1]/input.13
        self.module_6 = py_nndct.nn.Conv2d(in_channels=16, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[2]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.17
        self.module_7 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[2]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.21
        self.module_8 = py_nndct.nn.Conv2d(in_channels=96, out_channels=96, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=96, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[2]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.23
        self.module_9 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[2]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.27
        self.module_10 = py_nndct.nn.Conv2d(in_channels=96, out_channels=24, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[2]/Sequential[conv]/Conv2d[2]/input.29
        self.module_11 = py_nndct.nn.Conv2d(in_channels=24, out_channels=144, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[3]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.33
        self.module_12 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[3]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.37
        self.module_13 = py_nndct.nn.Conv2d(in_channels=144, out_channels=144, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=144, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[3]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.39
        self.module_14 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[3]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.43
        self.module_15 = py_nndct.nn.Conv2d(in_channels=144, out_channels=24, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[3]/Sequential[conv]/Conv2d[2]/input.45
        self.module_16 = py_nndct.nn.Add() #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[3]/input.47
        self.module_17 = py_nndct.nn.Conv2d(in_channels=24, out_channels=144, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[4]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.49
        self.module_18 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[4]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.53
        self.module_19 = py_nndct.nn.Conv2d(in_channels=144, out_channels=144, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=144, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[4]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.55
        self.module_20 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[4]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.59
        self.module_21 = py_nndct.nn.Conv2d(in_channels=144, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[4]/Sequential[conv]/Conv2d[2]/input.61
        self.module_22 = py_nndct.nn.Conv2d(in_channels=32, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[5]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.65
        self.module_23 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[5]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.69
        self.module_24 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=192, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[5]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.71
        self.module_25 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[5]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.75
        self.module_26 = py_nndct.nn.Conv2d(in_channels=192, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[5]/Sequential[conv]/Conv2d[2]/input.77
        self.module_27 = py_nndct.nn.Add() #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[5]/input.79
        self.module_28 = py_nndct.nn.Conv2d(in_channels=32, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[6]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.81
        self.module_29 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[6]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.85
        self.module_30 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=192, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[6]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.87
        self.module_31 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[6]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.91
        self.module_32 = py_nndct.nn.Conv2d(in_channels=192, out_channels=32, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[6]/Sequential[conv]/Conv2d[2]/input.93
        self.module_33 = py_nndct.nn.Add() #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[6]/input.95
        self.module_34 = py_nndct.nn.Conv2d(in_channels=32, out_channels=192, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[7]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.97
        self.module_35 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[7]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.101
        self.module_36 = py_nndct.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=192, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[7]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.103
        self.module_37 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[7]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.107
        self.module_38 = py_nndct.nn.Conv2d(in_channels=192, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[7]/Sequential[conv]/Conv2d[2]/input.109
        self.module_39 = py_nndct.nn.Conv2d(in_channels=64, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[8]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.113
        self.module_40 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[8]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.117
        self.module_41 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=384, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[8]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.119
        self.module_42 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[8]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.123
        self.module_43 = py_nndct.nn.Conv2d(in_channels=384, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[8]/Sequential[conv]/Conv2d[2]/input.125
        self.module_44 = py_nndct.nn.Add() #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[8]/input.127
        self.module_45 = py_nndct.nn.Conv2d(in_channels=64, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[9]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.129
        self.module_46 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[9]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.133
        self.module_47 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=384, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[9]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.135
        self.module_48 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[9]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.139
        self.module_49 = py_nndct.nn.Conv2d(in_channels=384, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[9]/Sequential[conv]/Conv2d[2]/input.141
        self.module_50 = py_nndct.nn.Add() #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[9]/input.143
        self.module_51 = py_nndct.nn.Conv2d(in_channels=64, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[10]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.145
        self.module_52 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[10]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.149
        self.module_53 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=384, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[10]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.151
        self.module_54 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[10]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.155
        self.module_55 = py_nndct.nn.Conv2d(in_channels=384, out_channels=64, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[10]/Sequential[conv]/Conv2d[2]/input.157
        self.module_56 = py_nndct.nn.Add() #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[10]/input.159
        self.module_57 = py_nndct.nn.Conv2d(in_channels=64, out_channels=384, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[11]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.161
        self.module_58 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[11]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.165
        self.module_59 = py_nndct.nn.Conv2d(in_channels=384, out_channels=384, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=384, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[11]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.167
        self.module_60 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[11]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.171
        self.module_61 = py_nndct.nn.Conv2d(in_channels=384, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[11]/Sequential[conv]/Conv2d[2]/input.173
        self.module_62 = py_nndct.nn.Conv2d(in_channels=96, out_channels=576, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[12]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.177
        self.module_63 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[12]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.181
        self.module_64 = py_nndct.nn.Conv2d(in_channels=576, out_channels=576, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=576, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[12]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.183
        self.module_65 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[12]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.187
        self.module_66 = py_nndct.nn.Conv2d(in_channels=576, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[12]/Sequential[conv]/Conv2d[2]/input.189
        self.module_67 = py_nndct.nn.Add() #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[12]/input.191
        self.module_68 = py_nndct.nn.Conv2d(in_channels=96, out_channels=576, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[13]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.193
        self.module_69 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[13]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.197
        self.module_70 = py_nndct.nn.Conv2d(in_channels=576, out_channels=576, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=576, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[13]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.199
        self.module_71 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[13]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.203
        self.module_72 = py_nndct.nn.Conv2d(in_channels=576, out_channels=96, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[13]/Sequential[conv]/Conv2d[2]/input.205
        self.module_73 = py_nndct.nn.Add() #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[13]/input.207
        self.module_74 = py_nndct.nn.Conv2d(in_channels=96, out_channels=576, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[14]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.209
        self.module_75 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[14]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.213
        self.module_76 = py_nndct.nn.Conv2d(in_channels=576, out_channels=576, kernel_size=[3, 3], stride=[2, 2], padding=[1, 1], dilation=[1, 1], groups=576, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[14]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.215
        self.module_77 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[14]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.219
        self.module_78 = py_nndct.nn.Conv2d(in_channels=576, out_channels=160, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[14]/Sequential[conv]/Conv2d[2]/input.221
        self.module_79 = py_nndct.nn.Conv2d(in_channels=160, out_channels=960, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[15]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.225
        self.module_80 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[15]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.229
        self.module_81 = py_nndct.nn.Conv2d(in_channels=960, out_channels=960, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=960, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[15]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.231
        self.module_82 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[15]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.235
        self.module_83 = py_nndct.nn.Conv2d(in_channels=960, out_channels=160, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[15]/Sequential[conv]/Conv2d[2]/input.237
        self.module_84 = py_nndct.nn.Add() #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[15]/input.239
        self.module_85 = py_nndct.nn.Conv2d(in_channels=160, out_channels=960, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[16]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.241
        self.module_86 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[16]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.245
        self.module_87 = py_nndct.nn.Conv2d(in_channels=960, out_channels=960, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=960, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[16]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.247
        self.module_88 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[16]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.251
        self.module_89 = py_nndct.nn.Conv2d(in_channels=960, out_channels=160, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[16]/Sequential[conv]/Conv2d[2]/input.253
        self.module_90 = py_nndct.nn.Add() #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[16]/input.255
        self.module_91 = py_nndct.nn.Conv2d(in_channels=160, out_channels=960, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[17]/Sequential[conv]/ConvNormActivation[0]/Conv2d[0]/input.257
        self.module_92 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[17]/Sequential[conv]/ConvNormActivation[0]/ReLU[2]/input.261
        self.module_93 = py_nndct.nn.Conv2d(in_channels=960, out_channels=960, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=960, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[17]/Sequential[conv]/ConvNormActivation[1]/Conv2d[0]/input.263
        self.module_94 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[17]/Sequential[conv]/ConvNormActivation[1]/ReLU[2]/input.267
        self.module_95 = py_nndct.nn.Conv2d(in_channels=960, out_channels=320, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/InvertedResidual[features]/InvertedResidual[17]/Sequential[conv]/Conv2d[2]/input.269
        self.module_96 = py_nndct.nn.Conv2d(in_channels=320, out_channels=1280, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/MobileNetV2Encoder[encoder]/ConvNormActivation[features]/ConvNormActivation[18]/Conv2d[0]/input.273
        self.module_97 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/MobileNetV2Encoder[encoder]/ConvNormActivation[features]/ConvNormActivation[18]/ReLU[2]/x.3
        self.module_98 = py_nndct.nn.Interpolate() #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[0]/11926
        self.module_99 = py_nndct.nn.Cat() #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[0]/input.277
        self.module_100 = py_nndct.nn.Conv2d(in_channels=1376, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[0]/Conv2dReLU[conv1]/Conv2d[0]/input.279
        self.module_101 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[0]/Conv2dReLU[conv1]/ReLU[2]/input.283
        self.module_102 = py_nndct.nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[0]/Conv2dReLU[conv2]/Conv2d[0]/input.285
        self.module_103 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[0]/Conv2dReLU[conv2]/ReLU[2]/x.5
        self.module_104 = py_nndct.nn.Interpolate() #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[1]/11990
        self.module_105 = py_nndct.nn.Cat() #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[1]/input.289
        self.module_106 = py_nndct.nn.Conv2d(in_channels=288, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[1]/Conv2dReLU[conv1]/Conv2d[0]/input.291
        self.module_107 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[1]/Conv2dReLU[conv1]/ReLU[2]/input.295
        self.module_108 = py_nndct.nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[1]/Conv2dReLU[conv2]/Conv2d[0]/input.297
        self.module_109 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[1]/Conv2dReLU[conv2]/ReLU[2]/x.7
        self.module_110 = py_nndct.nn.Interpolate() #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[2]/12054
        self.module_111 = py_nndct.nn.Cat() #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[2]/input.301
        self.module_112 = py_nndct.nn.Conv2d(in_channels=152, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[2]/Conv2dReLU[conv1]/Conv2d[0]/input.303
        self.module_113 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[2]/Conv2dReLU[conv1]/ReLU[2]/input.307
        self.module_114 = py_nndct.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[2]/Conv2dReLU[conv2]/Conv2d[0]/input.309
        self.module_115 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[2]/Conv2dReLU[conv2]/ReLU[2]/x.9
        self.module_116 = py_nndct.nn.Interpolate() #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[3]/12118
        self.module_117 = py_nndct.nn.Cat() #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[3]/input.313
        self.module_118 = py_nndct.nn.Conv2d(in_channels=80, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[3]/Conv2dReLU[conv1]/Conv2d[0]/input.315
        self.module_119 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[3]/Conv2dReLU[conv1]/ReLU[2]/input.319
        self.module_120 = py_nndct.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[3]/Conv2dReLU[conv2]/Conv2d[0]/input.321
        self.module_121 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[3]/Conv2dReLU[conv2]/ReLU[2]/x
        self.module_122 = py_nndct.nn.Interpolate() #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[4]/input.325
        self.module_123 = py_nndct.nn.Conv2d(in_channels=32, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[4]/Conv2dReLU[conv1]/Conv2d[0]/input.327
        self.module_124 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[4]/Conv2dReLU[conv1]/ReLU[2]/input.331
        self.module_125 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[4]/Conv2dReLU[conv2]/Conv2d[0]/input.333
        self.module_126 = py_nndct.nn.ReLU(inplace=True) #Unet::Unet/UnetDecoder[decoder]/DecoderBlock[blocks]/ModuleList[4]/Conv2dReLU[conv2]/ReLU[2]/input
        self.module_127 = py_nndct.nn.Conv2d(in_channels=16, out_channels=4, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=True) #Unet::Unet/SegmentationHead[segmentation_head]/Conv2d[0]/12255

    def forward(self, *args):
        output_module_0 = self.module_0(input=args[0])
        output_module_0 = self.module_1(output_module_0)
        output_module_0 = self.module_2(output_module_0)
        output_module_0 = self.module_3(output_module_0)
        output_module_0 = self.module_4(output_module_0)
        output_module_0 = self.module_5(output_module_0)
        output_module_6 = self.module_6(output_module_0)
        output_module_6 = self.module_7(output_module_6)
        output_module_6 = self.module_8(output_module_6)
        output_module_6 = self.module_9(output_module_6)
        output_module_6 = self.module_10(output_module_6)
        output_module_11 = self.module_11(output_module_6)
        output_module_11 = self.module_12(output_module_11)
        output_module_11 = self.module_13(output_module_11)
        output_module_11 = self.module_14(output_module_11)
        output_module_11 = self.module_15(output_module_11)
        output_module_16 = self.module_16(input=output_module_6, other=output_module_11, alpha=1)
        output_module_17 = self.module_17(output_module_16)
        output_module_17 = self.module_18(output_module_17)
        output_module_17 = self.module_19(output_module_17)
        output_module_17 = self.module_20(output_module_17)
        output_module_17 = self.module_21(output_module_17)
        output_module_22 = self.module_22(output_module_17)
        output_module_22 = self.module_23(output_module_22)
        output_module_22 = self.module_24(output_module_22)
        output_module_22 = self.module_25(output_module_22)
        output_module_22 = self.module_26(output_module_22)
        output_module_27 = self.module_27(input=output_module_17, other=output_module_22, alpha=1)
        output_module_28 = self.module_28(output_module_27)
        output_module_28 = self.module_29(output_module_28)
        output_module_28 = self.module_30(output_module_28)
        output_module_28 = self.module_31(output_module_28)
        output_module_28 = self.module_32(output_module_28)
        output_module_33 = self.module_33(input=output_module_27, other=output_module_28, alpha=1)
        output_module_34 = self.module_34(output_module_33)
        output_module_34 = self.module_35(output_module_34)
        output_module_34 = self.module_36(output_module_34)
        output_module_34 = self.module_37(output_module_34)
        output_module_34 = self.module_38(output_module_34)
        output_module_39 = self.module_39(output_module_34)
        output_module_39 = self.module_40(output_module_39)
        output_module_39 = self.module_41(output_module_39)
        output_module_39 = self.module_42(output_module_39)
        output_module_39 = self.module_43(output_module_39)
        output_module_44 = self.module_44(input=output_module_34, other=output_module_39, alpha=1)
        output_module_45 = self.module_45(output_module_44)
        output_module_45 = self.module_46(output_module_45)
        output_module_45 = self.module_47(output_module_45)
        output_module_45 = self.module_48(output_module_45)
        output_module_45 = self.module_49(output_module_45)
        output_module_50 = self.module_50(input=output_module_44, other=output_module_45, alpha=1)
        output_module_51 = self.module_51(output_module_50)
        output_module_51 = self.module_52(output_module_51)
        output_module_51 = self.module_53(output_module_51)
        output_module_51 = self.module_54(output_module_51)
        output_module_51 = self.module_55(output_module_51)
        output_module_56 = self.module_56(input=output_module_50, other=output_module_51, alpha=1)
        output_module_56 = self.module_57(output_module_56)
        output_module_56 = self.module_58(output_module_56)
        output_module_56 = self.module_59(output_module_56)
        output_module_56 = self.module_60(output_module_56)
        output_module_56 = self.module_61(output_module_56)
        output_module_62 = self.module_62(output_module_56)
        output_module_62 = self.module_63(output_module_62)
        output_module_62 = self.module_64(output_module_62)
        output_module_62 = self.module_65(output_module_62)
        output_module_62 = self.module_66(output_module_62)
        output_module_67 = self.module_67(input=output_module_56, other=output_module_62, alpha=1)
        output_module_68 = self.module_68(output_module_67)
        output_module_68 = self.module_69(output_module_68)
        output_module_68 = self.module_70(output_module_68)
        output_module_68 = self.module_71(output_module_68)
        output_module_68 = self.module_72(output_module_68)
        output_module_73 = self.module_73(input=output_module_67, other=output_module_68, alpha=1)
        output_module_74 = self.module_74(output_module_73)
        output_module_74 = self.module_75(output_module_74)
        output_module_74 = self.module_76(output_module_74)
        output_module_74 = self.module_77(output_module_74)
        output_module_74 = self.module_78(output_module_74)
        output_module_79 = self.module_79(output_module_74)
        output_module_79 = self.module_80(output_module_79)
        output_module_79 = self.module_81(output_module_79)
        output_module_79 = self.module_82(output_module_79)
        output_module_79 = self.module_83(output_module_79)
        output_module_84 = self.module_84(input=output_module_74, other=output_module_79, alpha=1)
        output_module_85 = self.module_85(output_module_84)
        output_module_85 = self.module_86(output_module_85)
        output_module_85 = self.module_87(output_module_85)
        output_module_85 = self.module_88(output_module_85)
        output_module_85 = self.module_89(output_module_85)
        output_module_90 = self.module_90(input=output_module_84, other=output_module_85, alpha=1)
        output_module_90 = self.module_91(output_module_90)
        output_module_90 = self.module_92(output_module_90)
        output_module_90 = self.module_93(output_module_90)
        output_module_90 = self.module_94(output_module_90)
        output_module_90 = self.module_95(output_module_90)
        output_module_90 = self.module_96(output_module_90)
        output_module_90 = self.module_97(output_module_90)
        output_module_90 = self.module_98(input=output_module_90, size=None, scale_factor=[2.0,2.0], mode='nearest')
        output_module_90 = self.module_99(dim=1, tensors=[output_module_90,output_module_73])
        output_module_90 = self.module_100(output_module_90)
        output_module_90 = self.module_101(output_module_90)
        output_module_90 = self.module_102(output_module_90)
        output_module_90 = self.module_103(output_module_90)
        output_module_90 = self.module_104(input=output_module_90, size=None, scale_factor=[2.0,2.0], mode='nearest')
        output_module_90 = self.module_105(dim=1, tensors=[output_module_90,output_module_33])
        output_module_90 = self.module_106(output_module_90)
        output_module_90 = self.module_107(output_module_90)
        output_module_90 = self.module_108(output_module_90)
        output_module_90 = self.module_109(output_module_90)
        output_module_90 = self.module_110(input=output_module_90, size=None, scale_factor=[2.0,2.0], mode='nearest')
        output_module_90 = self.module_111(dim=1, tensors=[output_module_90,output_module_16])
        output_module_90 = self.module_112(output_module_90)
        output_module_90 = self.module_113(output_module_90)
        output_module_90 = self.module_114(output_module_90)
        output_module_90 = self.module_115(output_module_90)
        output_module_90 = self.module_116(input=output_module_90, size=None, scale_factor=[2.0,2.0], mode='nearest')
        output_module_90 = self.module_117(dim=1, tensors=[output_module_90,output_module_0])
        output_module_90 = self.module_118(output_module_90)
        output_module_90 = self.module_119(output_module_90)
        output_module_90 = self.module_120(output_module_90)
        output_module_90 = self.module_121(output_module_90)
        output_module_90 = self.module_122(input=output_module_90, size=None, scale_factor=[2.0,2.0], mode='nearest')
        output_module_90 = self.module_123(output_module_90)
        output_module_90 = self.module_124(output_module_90)
        output_module_90 = self.module_125(output_module_90)
        output_module_90 = self.module_126(output_module_90)
        output_module_90 = self.module_127(output_module_90)
        return output_module_90
