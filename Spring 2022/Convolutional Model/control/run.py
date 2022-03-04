from numpy import array, savetxt
import ctypes
from os import scandir, remove
import paint_gui
from tkinter import *
from keras.models import load_model
from PIL import Image

def check():
	confirm = ctypes.windll.user32.MessageBoxW(0, "Performing this action will write over results.csv and all images " + 
		"in generated images. Are you sure you want to do this?", "Are you sure?", 1)
	if confirm == 1:
		print("Removing old images from generated_images...")
		try:
			for file in scandir("generated_images"):
				remove(file.path)
		except:
			print("generated_images doesn't exist.")
		print("Removing results.csv...")
		try:
			remove("results.csv")
		except:
			print("reults.csv doesn't exist.")
		print("Removed.")
		return;
	else:
		quit()

def run_test_images(model):
	data = array([array(Image.open(file.path)) for file in scandir("generated_images")])
	data = data.reshape((data.shape[0], 20, 20, 1))
	data = data.astype('float32')
	data = data / 255.0

	model = load_model(model)
	return model.predict(data)

def output_results(results):
	print("\nLaser outputs:")
	for result in results:
		print(result)
	savetxt("results.csv", results, delimiter=",")
	ctypes.windll.user32.MessageBoxW(0, "Laser patterns have been output to the terminal and results.csv", "Confirmation", 0)

class ModelPrompt:
	def __init__(self):
		self.prompt = Tk()
		self.L1 = Label(self.prompt, text="Model name").grid(row=0, column=0)
		self.E1 = Entry(self.prompt, bd =5)
		self.E1.grid(row=0, column=2)
		self.prompt.bind("<Return>", self.save_model)
		self.button1 = Button(self.prompt, text="Enter", command=self.save_model).grid(row=1, column=1)
		self.prompt.mainloop()

	def get_model(self):
		return self.model

	def save_model(self, event=None):
		self.model = self.E1.get()
		self.prompt.destroy()

def main():
	check()
	paint_gui.main()
	prompt = ModelPrompt()
	model = prompt.get_model()
	results = run_test_images(model)
	output_results(results)

if __name__ == "__main__":
	main()