from os import makedirs
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageDraw

class ImageDrawing:
	def __init__(self):
		self.ask = Tk()
		self.ask.title("Set folder name and counter")
		Label(self.ask, text="What folder should the images be saved in?").pack()
		self.name = Entry(self.ask, bd=5)
		self.name.pack()
		Label(self.ask, text="What number should the counter start with?").pack()
		self.count = Entry(self.ask, bd=5)
		self.count.pack()
		self.ask.bind("<Return>", self.set_vars)
		Button(self.ask, text="Enter", command=self.set_vars).pack()
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
		self.drawing_area.create_rectangle(95, 0, 105, 5, fill="white")
		Button(parent, text="Clear", command=self.clear_canvas).pack()
		Button(parent, text="Save", command=self.save).pack()
		parent.bind("<Return>", self.save)
		parent.bind("<BackSpace>", self.clear_canvas)
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
				event.widget.create_line(self.xold, self.yold, event.x,event.y,smooth=TRUE, width=10, fill="white")
				self.draw.line(((self.xold, self.yold), (event.x,event.y)), 1, width=20)
			self.xold = event.x
			self.yold = event.y

	def save(self):
		self.image.convert("L").resize((20, 20)).save("{folder_name}\generated_{i}.bmp".format(i = self.counter, folder_name = self.folder))
		messagebox.showinfo("Image saved", "Saved as generated_{i}.bmp in folder {folder_name}".format(i = self.counter, folder_name = self.folder))
		self.counter += 1
		self.clear_canvas()

	def set_vars(self, event=None):
		folder = self.name.get()
		count = self.count.get()
		if (folder and count):
			confirm = messagebox.askokcancel("Warning", "This process may overwrite images in {folder_name} with label greater than or equal to {count}.".format(folder_name = folder, count = int(count)))
			if confirm:
				self.folder = folder
				makedirs(self.folder, exist_ok=True)
				self.counter = int(count)
				self.ask.destroy()
				self.canvas()

	def get_folder(self):
		return self.folder

def main():
	drawing = ImageDrawing()
	return drawing.get_folder()

if __name__ == "__main__":
	main()