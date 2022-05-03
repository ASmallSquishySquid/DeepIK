import ctypes
import PIL.Image
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from keras.callbacks import EarlyStopping
from os import scandir, removedirs, listdir
from tkinter import *

class VariableGetter:
	def __init__(self):
		self.top = Tk()
		self.top.title("Name Prompt")
		self.top.iconbitmap("resources/icons/question.ico")
		self.L1 = Label(self.top, text="Model name").grid(row=0, column=0)
		self.E1 = Entry(self.top, bd =5)
		self.E1.grid(row=0, column=2)
		self.L2 = Label(self.top, text="Image Folder").grid(row=1, column=0)
		self.E2 = Entry(self.top, bd =5)
		self.E2.grid(row=1, column=2)
		self.L3 = Label(self.top, text="Laser Data").grid(row=2, column=0)
		self.E3 = Entry(self.top, bd =5)
		self.E3.grid(row=2, column=2)
		self.top.bind("<Return>", self.get_vars_button)
		self.button1 = Button(self.top, text="Enter", command=self.get_vars_button).grid(row=3, column=1)
		self.top.mainloop()

	def get_model(self):
		return self.model
	
	def get_folder(self):
		return self.folder
	
	def get_csv(self):
		return self.csv

	def get_vars_button(self, event=None):
		self.model = self.E1.get()
		self.folder = self.E2.get()
		self.csv = self.E3.get()
		if self.model and self.folder and self.csv:
			self.top.destroy()
		else:
			if self.model == "":
				self.E1["bg"] = "misty rose"
			else:
				self.E1["bg"] = "snow"
			
			if self.folder == "":
				self.E2["bg"] = "misty rose"
			else:
				self.E2["bg"] = "snow"

			if self.csv == "":
				self.E3["bg"] = "misty rose"
			else:
				self.E3["bg"] = "snow"

def confirm(model):
	confirm = ctypes.windll.user32.MessageBoxW(0, "Performing this action will write over {folder} if it already exists. Are you sure you want to do this?".format(folder=model), "Are you sure?", 1)
	if confirm == 1:
		print("Removing {model}...".format(model=model))
		try:
			removedirs(model)
			print("Removed.")
		except:
			print("{model} doesn't exist.".format(model=model))
		return;
	else:
		quit()

# load all the data into a test set
def load_full_data(folder, data):
	dataX = np.array([np.array(PIL.Image.open("pat{i}t=16.bmp".format(i=i))) for i in range(1, 730)])
	if len(dataX) == 0:
		print("There were no images for time 16. Using all images in folder.")
		quit();
	dataX = dataX.reshape((dataX.shape[0], 35, 35, 1))
	dataX = dataX.astype('float32')
	dataX = dataX / 255.0
	dataY = pd.read_csv(data, header=None, delimiter=",").to_numpy()
	return dataX, dataY

# define cnn model
def create_model():
	model = Sequential()
	model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(35, 35, 1)))
	model.add(Flatten())
	model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
	model.add(Dense(6, activation="sigmoid"))
	# compile model
	opt = SGD(learning_rate=0.01, momentum=0.9)
	model.compile(optimizer=opt, loss='mse', metrics=['mae'])
	return model

def fit_model(model, features, labels, epochs, batch_size):
	stop = EarlyStopping(monitor = "loss", mode = "min", verbose = 1, patience = (epochs * 0.1))
	model.fit(features, labels, epochs = epochs, verbose = 1, callbacks=[stop], batch_size=batch_size, validation_split = 0)

# train the model
def train(folder, data, name):
	trainX, trainY = load_full_data(folder, data)
	model = create_model()
	fit_model(model, trainX, trainY, 1500, 100)
	model.save(name)

def main():
	vars = VariableGetter()
	confirm(vars.get_model())
	train(vars.get_folder(), vars.get_csv(), vars.get_model())

if __name__ == "__main__":
	main()