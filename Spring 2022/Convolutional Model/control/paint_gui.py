import ctypes
from os import scandir, remove, makedirs
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageDraw

class ImageDrawing:
	def __init__(self):
		self.ask = Tk()
		self.ask.title("Set counter")
		Label(self.ask, text="What number should the counter start with?").pack()
		self.text = Entry(self.ask, bd=5)
		self.text.pack()
		self.ask.bind("<Return>", self.get_count)
		Button(self.ask, text="Enter", command=self.get_count).pack()
		self.ask.mainloop()

	def canvas(self):
		parent = Tk()
		parent.title("Draw")
		self.b1 = "up"
		self.xold, self.yold = None, None
		self.drawing_area = Canvas(parent, width=200, height=200, bg="black")
		self.drawing_area.pack()
		self.drawing_area.bind("<Motion>", self.motion)
		self.drawing_area.bind("<ButtonPress-1>", self.b1down)
		self.drawing_area.bind("<ButtonRelease-1>", self.b1up)
		self.drawing_area.create_rectangle(90, 0, 110, 5, fill="white")
		Button(parent, text="Clear", command=self.clear_canvas).pack()
		Button(parent, text="Save", command=self.save).pack()
		self.image = Image.new("1",(200,200))
		self.draw = ImageDraw.Draw(self.image)
		parent.mainloop()

	def clear_canvas(self):
		self.drawing_area.delete("all")
		self.image=Image.new("1",(200,200))
		self.draw=ImageDraw.Draw(self.image)
		self.drawing_area.create_rectangle(90, 0, 110, 5, fill="white")

	def b1down(self, event):
		self.b1 = "down"

	def b1up(self, event):
		self.b1 = "up"
		self.xold = None           # reset the line when you let go of the button
		self.yold = None

	def motion(self, event):
		if self.b1 == "down":
			if self.xold is not None and self.yold is not None:
				event.widget.create_line(self.xold, self.yold, event.x,event.y,smooth=TRUE, width=20, fill="white")
				self.draw.line(((self.xold, self.yold), (event.x,event.y)), 1, width=20)
			self.xold = event.x
			self.yold = event.y

	def save(self):
		self.image.convert("L").resize((20, 20)).save("generated_images\generated_{i}.bmp".format(i = self.counter))
		messagebox.showinfo("Image saved", "Saved as generated_{i}.bmp in generated_images folder".format(i = self.counter))
		self.counter += 1
		self.clear_canvas()

	def get_count(self, event=None):
		self.counter = int(self.text.get())
		self.ask.destroy()
		self.canvas()

def check():
	confirm = ctypes.windll.user32.MessageBoxW(0, "Performing this action will write over all images " + 
		"in generated images. Are you sure you want to do this?", "Are you sure?", 1)
	if confirm == 1:
		print("Removing old images from generated_images...")
		try:
			for file in scandir("generated_images"):
				remove(file.path)
			print("Removed.")
		except:
			print("generated_images doesn't exist.")
			makedirs("generated_images")
		return;
	else:
		quit()

def main():
	ImageDrawing()

if __name__ == "__main__":
	check()
	main()