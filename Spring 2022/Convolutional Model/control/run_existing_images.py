from numpy import array
import ctypes
from os import scandir
from run import output_results
from tkinter import *
from PIL import Image
from keras.models import load_model

class VariableGetter:
	def __init__(self):
		self.top = Tk()
		self.L1 = Label(self.top, text="Model name").grid(row=0, column=0)
		self.E1 = Entry(self.top, bd =5)
		self.E1.grid(row=0, column=2)
		self.L2 = Label(self.top, text="Folder").grid(row=1, column=0)
		self.E2 = Entry(self.top, bd =5)
		self.E2.grid(row=1, column=2)
		self.top.bind("<Return>", self.get_vars_button)
		self.button1 = Button(self.top, text="Enter", command=self.get_vars_button).grid(row=3, column=1)
		self.top.mainloop()

	def get_model(self):
		return self.model
	
	def get_folder(self):
		return self.folder

	def get_vars_button(self, event=None):
		self.model = self.E1.get()
		self.folder = self.E2.get()
		self.top.destroy()

def confirm():
	confirm = ctypes.windll.user32.MessageBoxW(0, "Performing this action will write over results.csv. Are you sure you want to do this?", "Are you sure?", 1)
	if confirm != 1:
		quit()

def run_test_images(model, folder):
	print("\nProcessing...")
	data = array([array(Image.open(file.path).convert("L").resize([20, 20])) for file in scandir(folder) if file.name.endswith(".bmp") and file.is_file()])
	data = data.reshape((data.shape[0], 20, 20, 1))
	data = data.astype('float32')
	data = data / 255.0

	if len(data) == 0:
		ctypes.windll.user32.MessageBoxW(0, "There are no .bmp files in this folder", "No valid files", 0)
		print("Program terminated")
		quit()

	model = load_model(model)
	return model.predict(data)

def main():
	confirm()
	vars = VariableGetter()
	results = run_test_images(vars.get_model(), vars.get_folder())
	output_results(results)

if __name__ == "__main__":
	main()