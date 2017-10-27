# CNTK Evaluate Performance Test

This code is some test about using [CNTK](https://github.com/Microsoft/CNTK/) framework's evaluate performance, compare with [OpenCV DNN](https://docs.opencv.org/3.3.0/d2/d58/tutorial_table_of_content_dnn.html) module using caffe model.

## Test environment
#### Framework
* CNTK v2.2 ([CNTK.GPU](https://www.nuget.org/packages/CNTK.GPU/))
* Python 3.6.3 
* OpenCv 3.3.0.10 ([opencv-python](https://pypi.python.org/pypi/opencv-python))
* .NET Framework 4.6.1
#### System
* Windows 10 Pro 64bit
#### Hardware
* Intel Core i7-7820HQ @ 2.90GHz
* nVidia Quadro M1200

## Test Model
Deep Residual Networks a.k.a ResNet, this test choose ResNet50_ImageNet pre-trained model to test.
* CNTK model : [CNTK Pre-trained Models](https://github.com/Microsoft/CNTK/tree/master/PretrainedModels)
* Caffe model : [Deep Residual Networks](https://github.com/KaimingHe/deep-residual-networks)

## Test Image
Space Shuttle  
![Space Shuttle](CntkEvaluatePerformance/Common/space_shuttle.jpg "Space Shuttle")  
  

## Project Introduction
In this solution, we have 3 projects for 3 diffetent test.
* **CntkEvaluatePerformance** : Evaluate with CNTK in C#.
* **PythonCntk** : Evaluate with CNTK in python.
* **PythonOpencvDnn** : Evaluate with OpenCv DNN in python.  

Most code are almost follow example to keep it simple.

## Test Result 
* CNTK in C# : 1117ms 
![CNTK C# Result](https://i.imgur.com/KuiMnZ8.png "CNTK C# Result")  
* CNTK in Python : 1114ms
![CNTK C# Python](https://i.imgur.com/heo29pO.png "CNTK Python Result")  
* OpenCv DNN Caffe model in Python : 151ms 
![OpenCv DNN Result](https://i.imgur.com/sz78rUJ.png "OpenCv DNN Result")  


***Evaluate one image in CNTK does 7 times slower than evaluate in OpenCv DNN, Why ?***
