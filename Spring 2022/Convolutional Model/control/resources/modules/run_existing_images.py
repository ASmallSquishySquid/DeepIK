from numpy import array, savetxt
import ctypes
import os
from tkinter import *
import PIL.Image
import csv

class VariableGetter:
	def __init__(self):
		self.top = Tk()
		self.top.title("Name Prompt")
		self.top.iconbitmap("resources/icons/question.ico")
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
		if self.model and self.folder:
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

def confirm():
	confirm = ctypes.windll.user32.MessageBoxW(0, "Performing this action will write over run_order.csv and results.csv. Are you sure you want to do this?", "Are you sure?", 1)
	if confirm == 1:
		print("Removing results.csv...")
		try:
			os.remove("results.csv")
			print("Removed.")
		except:
			print("reults.csv doesn't exist.")

		print("Removing run_order.csv...")
		try:
			os.remove("run_order.csv")
			print("Removed.")
		except:
			print("run_order doesn't exist.")
		
		return;
	else:
		quit()

def run_test_images(model, folder):
	print("\nProcessing...")
	try:
		# Get list of all files only in the given directory
		list_of_files = filter(lambda x: os.path.isfile(os.path.join(folder, x)), os.listdir(folder))
		# Sort list of files based on last modification time in ascending order
		list_of_files = sorted(list_of_files,key = lambda x: os.path.getmtime(os.path.join(folder, x)))
		list_of_files = [file for file in list_of_files if file.endswith(".bmp")]
		print("File run order:")
		print(list_of_files)
		
		with open("run_order.csv", "w+", newline="") as f:
			write = csv.writer(f)
			files = array(list_of_files)
			files = files.reshape((files.shape[0], 1))
			write.writerows(files)

		data = array([array(PIL.Image.open("{folder}/{file}".format(folder=folder, file=file)).convert("L").resize([35, 35])) for file in list_of_files])

	except:
		ctypes.windll.user32.MessageBoxW(0, "This folder does not exist", "Not a valid folder", 0)
		print("Program terminated")
		quit()

	if len(data) == 0:
		ctypes.windll.user32.MessageBoxW(0, "There are no .bmp files in this folder", "No valid files", 0)
		print("Program terminated")
		quit()
	
	data = data.reshape((data.shape[0], 35, 35, 1))
	data = data.astype('float32')
	data = data / 255.0

	from keras.models import load_model
	try:
		model = load_model(model)
	except:
		ctypes.windll.user32.MessageBoxW(0, "This model does not exist", "Not a valid model", 0)
		print("Program terminated")
		quit()
	
	return model.predict(data)

def output_results(results):
	print("\nLaser outputs:")
	for result in results:
		print(result)
	savetxt("results.csv", results, delimiter=",")
	ctypes.windll.user32.MessageBoxW(0, "Laser patterns have been output to the terminal and results.csv", "Confirmation", 0)
	input() 

def main():
	confirm()
	vars = VariableGetter()
	results = run_test_images(vars.get_model(), vars.get_folder())
	output_results(results)

if __name__ == "__main__":
	main()