from keras.models import load_model
from PIL import Image
import numpy as np
import ctypes
import os

def check():
	confirm = ctypes.windll.user32.MessageBoxW(0, "Performing this action will write over results.csv and all images " + 
		"in generated images. Are you sure you want to do this?", "Are you sure?", 1)
	if confirm == 1:
		for file in os.scandir("generated_images"):
			os.remove(file.path)
		return;
	else:
		quit()

def run_test_images(model):
	data = np.array([np.array(Image.open(file.path)) for file in os.scandir("generated_images")])
	data = data.reshape((data.shape[0], 20, 20, 1))
	data = data.astype('float32')
	data = data / 255.0

	model = load_model(model)
	return model.predict(data)

def output_results(results):
	print("\nLaser outputs:")
	for result in results:
		print(result)
	np.savetxt("results.csv", results, delimiter=",")
	ctypes.windll.user32.MessageBoxW(0, "Laser patterns have been output to the terminal and results.csv", "Confirmation", 0)

if __name__ == "__main__":
	check()
	exec(open("paint_gui.py").read())
	print("Enter model name:")
	model = input()
	results = run_test_images(model)
	output_results(results)