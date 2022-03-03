from keras.models import load_model
from PIL import Image
import numpy as np
import pandas as pd
import shutil
from matplotlib import pyplot as plt

exec(open("paint_gui.py").read())

def run_test_images(model):
	data = np.array([np.array(Image.open("generated_images\generated_{i}.bmp".format(i = i))) for i in range(1, 6)])
	data = data.reshape((data.shape[0], 20, 20, 1))
	data = data.astype('float32')
	data = data / 255.0

	model = load_model(model)
	print(model.predict(data))

run_test_images("model_full_data")