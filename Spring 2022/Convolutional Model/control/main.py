from tkinter import *

def paint(event=None):
	top.destroy()
	import resources.modules.paint_gui as paint_gui
	paint_gui.main()

def existing(event=None):
	top.destroy()
	import resources.modules.run_existing_images as run_existing_images
	run_existing_images.main()

def run_all(event=None):
	top.destroy()
	import resources.modules.run as run
	run.main()

def build_model(event=None):
	top.destroy()
	import resources.modules.model as model
	model.main()

if __name__ == "__main__":
	top = Tk()
	top.title("Welcome!")
	top.iconbitmap("resources/icons/home.ico")
	top.configure(background="white")
	Label(top, text="Welcome to PS Paint! What would you like to do?", background="white").grid(row=0)
	top.bind("1", paint)
	top.bind("2", build_model)
	top.bind("3", existing)
	top.bind("4", run_all)
	Button(top, text="Draw new images (1)", command=paint, background="lemon chiffon").grid(row=1, padx=10, pady=5)
	Button(top, text="Train a new model (2)", command=build_model, background="papaya whip").grid(row=2, padx=10, pady=5)
	Button(top, text="Run a model on existing data (3)", command=existing, background="misty rose").grid(row=3, padx=10, pady=5)
	Button(top, text="Draw new images and run a model (4)", command=run_all, background="lavender").grid(row=4, padx=10, pady=5)
	top.mainloop()