# Utils

All scripts require Python 3.6.

## csv_to_images

Reads a csv file containing rows of pixels and outputs images into a specified directory. If running locally, requires [Pillow](http://pillow.readthedocs.io/) package to be installed.

```sh
python utils/csv_to_images.py -f <ABSOLUTE_PATH_TO>/Hw2_data/train_data.csv -o <ABSOLUTE_PATH_TO>/Hw2_data/images/training
```

![face_dataset](https://cloud.githubusercontent.com/assets/560721/25921032/c6045e44-3588-11e7-9458-6db13c0223d9.PNG)