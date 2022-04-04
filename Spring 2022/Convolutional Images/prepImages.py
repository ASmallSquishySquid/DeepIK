from PIL import Image

# for i in range(1, 730):
# 	im = Image.open("Spring 2022\\frames15t5Rewrite3\pat{i}t=5.bmp".format(i = i))
# 	left = 420
# 	right = 780
# 	top = 250
# 	bottom = 610
# 	im = im.crop((left, top, right, bottom))
# 	im = im.resize((20, 20))
# 	im.save("Spring 2022\\Convolutional Images\pat{i}.bmp".format(i = i))

def pad(num):
	import random
	import csv
	from PIL import ImageOps
	samples = random.sample(range(1, 730), num)
	i = 1
	for sample in samples:
		im = Image.open("Spring 2022\\Convolutional Images\pat{i}.bmp".format(i = sample))
		k = random.randint(0, 1)
		if k:
			im = ImageOps.expand(im, border=(0, 0, 5, 0), fill=(0))
			im = im.crop((5, 0, 40, 35))
		else:
			im = ImageOps.expand(im, border=(5, 0, 0, 0), fill=(0))
			im = im.crop((0, 0, 35, 35))
		im.save("Spring 2022\\Convolutional Images\pat{i}.bmp".format(i = 729 + i))
		i += 1

	with open("Spring 2022\Convolutional Model\\NewData.csv", "r", newline='') as file:
		read = csv.reader(file)
		rows = [row for idx, row in enumerate(read, 1) if idx in samples]
	
	with open("Spring 2022\Convolutional Model\\NewData.csv", "a", newline='') as file:
		write = csv.writer(file)
		write.writerows(rows)

		
pad(100)