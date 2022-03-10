from tkinter import *

def paint(event=None):
	top.destroy()
	import paint_gui
	paint_gui.main()

def existing(event=None):
	top.destroy()
	import run_existing_images
	run_existing_images.main()

def run_all(event=None):
	top.destroy()
	import run
	run.main()

if __name__ == "__main__":
	top = Tk()
	top.title("Welcome!")
	Label(top, text="What would you like to do?").grid(row=0, column=1)
	top.bind("1", paint)
	top.bind("2", existing)
	top.bind("3", run_all)
	Button(top, text="Draw new images (1)", command=paint).grid(row=1, column=0)
	Button(top, text="Run a model on existing data (2)", command=existing).grid(row=1, column=1)
	Button(top, text="Draw new images and run a model (3)", command=run_all).grid(row=1, column=2)
	top.mainloop()