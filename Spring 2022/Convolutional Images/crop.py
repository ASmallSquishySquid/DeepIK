from PIL import Image
from os import makedirs, scandir, rename, remove

makedirs("frames2_smol", exist_ok=True)

for file in scandir("frames2"):
	if file.is_file() and file.name.endswith("t=16.bmp"):
		im = Image.open(file.path)
		im = im.crop((358, 315, 1224, 1181))
		fn = lambda x : 255 if x > 140 else 0
		im = im.convert("L").point(fn, mode='1').resize((35, 35))
		im.save("frames2_smol/{i}".format(i = file.name))