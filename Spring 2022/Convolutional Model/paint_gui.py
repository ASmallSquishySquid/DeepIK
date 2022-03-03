# Paint program by Dave Michell. https://svn.python.org/projects/python/trunk/Demo/tkinter/guido/paint.py

from tkinter import *
from tkinter import messagebox
from PIL import Image

"""paint.py: not exactly a paint program.. just a smooth line drawing demo."""

b1 = "up"
xold, yold = None, None
counter = 1

def clear_canvas():
	drawing_area.delete("all")

def b1down(event):
	global b1
	b1 = "down"           # you only want to draw when the button is down
						  # because "Motion" events happen -all the time-

def b1up(event):
	global b1, xold, yold
	b1 = "up"
	xold = None           # reset the line when you let go of the button
	yold = None

def motion(event):
	if b1 == "down":
		global xold, yold
		if xold is not None and yold is not None:
			event.widget.create_line(xold,yold,event.x,event.y,smooth=TRUE, width=20)
						  # here's where you draw it. smooth. neat.
		xold = event.x
		yold = event.y

def save_as_png():
	global counter
	filename = "generated_images/generated_{i}".format(i = counter)
	# save postscipt image
	drawing_area.postscript(file = filename + ".eps")
	# use PIL to convert to PNG 
	img = Image.open(filename + '.eps')
	img = img.resize([20, 20])
	img.save(filename + '.bmp', 'bmp')
	messagebox.showinfo("Image saved", "Saved as hrgenerated_{i}.bmp in generated_images folder".format(i = counter))
	counter += 1
	
root = Tk()
drawing_area = Canvas(root, width=200, height=200)
drawing_area.pack()
drawing_area.bind("<Motion>", motion)
drawing_area.bind("<ButtonPress-1>", b1down)
drawing_area.bind("<ButtonRelease-1>", b1up)
button1 = Button(root, text="Clear", command=clear_canvas)
button1.pack()
button2 = Button(root, text="Save", command=save_as_png)
button2.pack()
root.mainloop()