from keras.models import load_model
from PIL import Image
import numpy as np
import ctypes
import os
from run import output_results
from tkinter import *

model = "";
folder = "";

def confirm():
	confirm = ctypes.windll.user32.MessageBoxW(0, "Performing this action will write over results.csv. Are you sure you want to do this?", "Are you sure?", 1)
	if confirm != 1:
		quit()

def get_vars():
	top = Tk()
	L1 = Label(top, text="Model name")
	L1.pack( side = LEFT)
	E1 = Entry(top, bd =5)
	E1.pack(side = RIGHT)
	L2 = Label(top, text="Folder")
	L2.pack( side = LEFT)
	E2 = Entry(top, bd =5)
	E2.pack(side = RIGHT)
	button1 = Button(top, text="Enter", command=get_vars_helper)
	button1.pack()
	top.mainloop()

def get_vars_helper():
	pass

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