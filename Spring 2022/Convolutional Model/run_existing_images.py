from keras.models import load_model
from PIL import Image
import numpy as np
import ctypes
import os
from run import output_results

model = "";
folder = "";

def confirm():
	confirm = ctypes.windll.user32.MessageBoxW(0, "Performing this action will write over results.csv. Are you sure you want to do this?", "Are you sure?", 1)
	if confirm != 1:
		quit()

def get_vars():
	global model, folder
	print("Please input model name:")
	model = input()
	print("Please input folder name:")
	folder = input()

def run_test_images(model):
	print("\nProcessing...")
	data = np.array([np.array(Image.open(file.path)) for file in os.scandir(folder)])
	data = data.reshape((data.shape[0], 20, 20, 1))
	data = data.astype('float32')
	data = data / 255.0
	model = load_model(model)
	return model.predict(data)

if __name__ == "__main__":
	confirm()
	get_vars()
	results = run_test_images(model)
	output_results(results)