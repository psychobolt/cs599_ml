#!/bin/bash
nohup tensorboard --logdir=/root/workspace/notebooks/Graph > /root/workspace/tensorboard.log 2>&1&
jupyter notebook --notebook-dir=/root/workspace/notebooks --ip='*' --port=8888 --no-browse