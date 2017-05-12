[![Stories in Ready](https://badge.waffle.io/psychobolt/cs599_ml.png?label=ready&title=Ready)](https://waffle.io/psychobolt/cs599_ml)
# cs599_ml

Repository for my work in a Machine Learning course

## Development

You can set up Docker or install locally.

### Local Install (Tensorflow GPU support)

Install Anaconda and create a environment:

```sh
conda create -n tensorflow-gpu
# or using a specified path
conda create -p <yourOwnPythonEnvDir>
```

Install using Conda and Pip:

```(tensorflow-gpu) $ conda install scipy && conda install scikit-learn && conda install pandas && pip install matplotlib jupyter keras```

> For more details see [here](https://www.quora.com/How-can-I-work-with-Keras-on-a-Jupyter-notebook-using-Tensorflow-as-backend).

(Windows) See [guide](https://nitishmutha.github.io/tensorflow/2017/01/22/TensorFlow-with-gpu-for-windows.html) to install setup CUDA.

#### Running Jupyter

```sh
$ (tensorflow-gpu) $ jupyter notebook --notebook-dir=<ABSOLUTE_PATH_TO>/jupyter_notebooks
```

### Docker (CPU support only)

#### Build Docker Image

```sh
docker build -t cs599_ml/anaconda3 .
```

> "." refers to the Dockerfile directory. The assumption is you're in the cs599_ml directory

#### Running Jupyter Container

```sh
docker run -it -p 8888:8888 -p 6006:6006 -v <ABSOLUTE_PATH_TO>/jupyter_notebooks:/root/workspace/notebooks cs599_ml/anaconda3
```

#### Interactive Bash

Use the same command as Jupyter notebook but append ``` /bin/bash``` to the end (including space). Exclude the port mapping, if jupyter container is running.

```sh
# For installing libraries, run the following commands: 
pip install <PACKAGE_NAME>
pip freeze > requirements.txt
# then exit bash and commit/push requirements.txt

# Run python scripts
python my_script.py
```

> Rebuild docker image after installing new libraries.

## Utils

See [utils/](utils/)
