from PIL import Image
from os import makedirs, scandir, rename, remove

makedirs("frames6_smol", exist_ok=True)

for file in scandir("frames6"):
	if file.is_file() and file.name.endswith("t=16.bmp"):
		im = Image.open(file.path)
		im = im.crop((358, 315, 1224, 1181))
		fn = lambda x : 255 if x > 140 else 0
		im = im.convert("L").point(fn, mode='1').resize((35, 35))
		im.save("frames6_smol/{i}".format(i = file.name))

# for i in range(1, 730):
# 	remove("Spring 2022\Convolutional Images\pat{i}.bmp".format(i = i))
# 	rename("Spring 2022\Convolutional Images\pat{i}t=16.bmp".format(i = i), "Spring 2022\Convolutional Images\pat{i}.bmp".format(i = i))