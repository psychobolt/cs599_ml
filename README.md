# cs599_ml

Repository for my work in a Machine Learning course

## Environment Setup

1. Install Docker
2. ```docker build -t cs599_ml/anaconda3 .```

> "." refers to the Dockerfile directory. The assumption is you're in the cs599_ml directory

## Terminal

```sh
docker run -it cs599_ml/anaconda3 /bin/bash
```

## Running Jupyter

```sh
docker run -it -p 8888:8888 -v <ABSOLUTE_PATH_TO>/jupyter_notebooks:/opt/notebooks cs599_ml/anaconda3
```