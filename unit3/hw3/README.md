# Homework 3

## Setup Instructions

I ran my code on TensorFlow using an NVIDIA GPU, and the current code assumes a valid GPU installation of TensorFlow. This means you will need to have all of the required CUDA and cuDNN libraries needed to run the TensorFlow2 on a GPU.

For complete reproducibility, I am using CUDA 10.1 and cuDNN v7.6.5, but this code should still run just fine on other versions of both, provided that they are compatible with your TensorFlow version. My conda environment configuration, containing TensorFlow 2.3.1 and `matplotlib`, is available in both environment files: `environment_concise.yml` (for only the most required dependences, and which also works cross-platform), and `environment_verbose.yml` (which is a complete dump of every system-specific conda and pip package I used).

Install the dependencies and activate my conda environment by running:

```bash
# create the environment:

# concise, cross-platform version
conda env create -f environment_concise.yml

# OR

# verbose version (exactly what I used)
conda env create -f environment_verbose.yml

# activate the env
conda activate tf2
```

## Running

### Quickstart (Assignment Step 1)

How I confirm that my TensorFlow GPU installation is valid:

In an interactive `python` shell (run `python` in the env):

```python
import tensorflow as tf
tf.config.list_physical_devices('GPU')
```

This produces the following output on my machine:

```python
>>> import tensorflow as tf
2020-12-03 22:12:45.590360: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cudart64_101.dll
>>> tf.config.list_physical_devices('GPU')
2020-12-03 22:12:57.230780: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library nvcuda.dll
2020-12-03 22:12:57.312002: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1716] Found device 0 with properties: 
pciBusID: 0000:01:00.0 name: GeForce RTX 2070 computeCapability: 7.5
coreClock: 1.44GHz coreCount: 36 deviceMemorySize: 8.00GiB deviceMemoryBandwidth: 417.29GiB/s
2020-12-03 22:12:57.342340: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cudart64_101.dll    
2020-12-03 22:12:57.349134: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cublas64_10.dll
2020-12-03 22:12:57.357129: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cufft64_10.dll
2020-12-03 22:12:57.361711: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library curand64_10.dll
2020-12-03 22:12:57.370262: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cusolver64_10.dll
2020-12-03 22:12:57.383548: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cusparse64_10.dll
2020-12-03 22:12:57.396580: I tensorflow/stream_executor/platform/default/dso_loader.cc:48] Successfully opened dynamic library cudnn64_7.dll
2020-12-03 22:12:57.425865: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1858] Adding visible gpu devices: 0
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

All libraries load properly and my GPU is detected, so it's clear that the installation was successful and that TensorFlow will use the GPU.

### CatDogMonkey (Assignments Steps 2 and 3)

Open the Jupyter notebook *after enabling the conda environment* by running `jupyter notebook` in this directory. If you run into problems where the modules in the environment are not detected (i.e. `ImportErrors` with tensorflow or matplotlib), ensure you have the `ipykernel` module installed. Also make sure the kernel is pointing to the correct python environment by running:

```bash
python -m ipykernel install --user --name=tf2
```