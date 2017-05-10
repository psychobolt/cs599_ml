# coding: utf-8

'''
This script creates 3-channel gray images from a csv.
It has been done so that the CNNs designed for RGB images can 
be used without modifying the input shape. 

This is a modified script requires two command line parameters:
1. The path to the CSV file
2. The output directory

It generates the images and saves them in a specified directory.

Original script: https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/discussion/29428
'''

import os
import csv
import argparse
import numpy as np 
import scipy.misc

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', required=True, help="path of the csv file")
parser.add_argument('-o', '--output', required=True, help="path of the output directory")

args = parser.parse_args()

w, h = 48, 48
image = np.zeros((h, w), dtype=np.uint8)
id = 1
with open(args.file, 'r') as csvfile:
    datareader = csv.reader(csvfile, delimiter =',')
    for row in datareader: 
        pixels_array = np.asarray(row, dtype=np.uint)

        image = pixels_array.reshape(w, h)
        # print(image.shape)

        stacked_image = np.dstack((image,) * 3)
        # print(stacked_image.shape)

        image_folder = os.path.join(args.output)
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        image_file =  os.path.join(image_folder , str(id) + '.jpg')
        scipy.misc.imsave(image_file, stacked_image)
        id += 1 
        if id % 100 == 0:
            print('Processed {} images'.format(id))

print("Finished processing {} images".format(id))
