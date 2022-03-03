# Paint program by Dave Michell. https://svn.python.org/projects/python/trunk/Demo/tkinter/guido/paint.py

from tkinter import *
from tkinter import messagebox
from PIL import ImageGrab
from PIL import Image
from PIL import ImageDraw

class ImageDrawing:
	def __init__(self, parent):
		self.parent = parent
		self.b1 = "up"
		self.xold, self.yold = None, None
		self.counter = 1
		self.drawing_area = Canvas(root, width=200, height=200, bg="black")
		self.drawing_area.pack()
		self.drawing_area.bind("<Motion>", self.motion)
		self.drawing_area.bind("<ButtonPress-1>", self.b1down)
		self.drawing_area.bind("<ButtonRelease-1>", self.b1up)
		self.drawing_area.create_rectangle(90, 0, 110, 5, fill="white")
		self.button1 = Button(root, text="Clear", command=self.clear_canvas)
		self.button1.pack()
		self.button2 = Button(root, text="Save", command=self.save)
		self.button2.pack()
		self.image = Image.new("1",(200,200))
		self.draw = ImageDraw.Draw(self.image)

	def clear_canvas(self):
		self.drawing_area.delete("all")
		self.image=Image.new("1",(200,200))
		self.draw=ImageDraw.Draw(self.image)

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
		self.image.convert("L").resize((20, 20)).save("generated_images\generated_{i}.bmp".format(i = counter))
		messagebox.showinfo("Image saved", "Saved as generated_{i}.bmp in generated_images folder".format(i = counter))
		self.counter += 1
		self.clear_canvas()

if __name__ == "__main__":
	root = Tk()
	root.title("Draw")
	ImageDrawing(root)
	root.mainloop()