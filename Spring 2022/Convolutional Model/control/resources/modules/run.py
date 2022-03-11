import ctypes
from os import remove
import resources.modules.paint_gui as paint_gui
from resources.modules.run_existing_images import run_test_images, output_results
from tkinter import *

def check():
	confirm = ctypes.windll.user32.MessageBoxW(0, "Performing this action will write over results.csv and potentially some images " + 
		"in the provided folder. Are you sure you want to do this?", "Are you sure?", 1)
	if confirm == 1:
		print("Removing results.csv...")
		try:
			remove("results.csv")
			print("Removed.")
		except:
			print("reults.csv doesn't exist.")
		return;
	else:
		quit()

class ModelPrompt:
	def __init__(self):
		self.prompt = Tk()
		self.prompt.title("Name Prompt")
		self.prompt.iconbitmap("resources/icons/question.ico")
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
		if self.model:
			self.prompt.destroy()
		else:
			self.E1["bg"] = "misty rose"

def main():
	check()
	folder = paint_gui.main()
	prompt = ModelPrompt()
	model = prompt.get_model()
	results = run_test_images(model, folder)
	output_results(results)

if __name__ == "__main__":
	main()