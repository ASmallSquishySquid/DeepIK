from PIL import Image

for i in range(1, 730):
	im = Image.open("Spring 2022\\frames15t5Rewrite3\pat{i}t=5.bmp".format(i = i))
	left = 420
	right = 780
	top = 250
	bottom = 610
	im = im.crop((left, top, right, bottom))
	im = im.resize((20, 20))
	im.save("Spring 2022\\Convolutional Images\pat{i}.bmp".format(i = i))