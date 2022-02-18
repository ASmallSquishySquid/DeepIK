from keras.models import load_model
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc
import math

data = np.array([np.array(Image.open("Spring 2022\Convolutional Model\\test_images\{i}.bmp".format(i = i)).convert('L')) for i in range(1, 6)])
data = data.reshape((data.shape[0], 20, 20, 1))
data = data.astype('float32')
data = data / 255.0

model = load_model("Spring 2022\Convolutional Model\model")
results = list(model.predict(data))

# plot robot path
def f(power):
	return max([0, 25 * (power - 1)])

def dependent(p1, p2, p3, length):
	theta1 = math.radians(f(p1))
	theta2 = math.radians(f(p2))
	theta3 = math.radians(f(p3))
	length1 = length / 4
	length2 = min([length - length1, abs(length / (4 * math.cos(theta1)))])
	length3 = min([length - length1 - length2, abs(length / (4 * math.cos(theta1 + theta2)))])
	length4 = max([0, length - length1 - length2 - length3])
	return theta1, theta2, theta3, length1, length2, length3, length4

def calc_points(pow1, pow2, pow3, length):
	save = dependent(pow1, pow2, pow3, length)
	lines = [[(0, 0), (0, save[3])]]
	end = (0, save[3])
	theta = 0
	for i in range(3):
		lines.append([end, calc_end(save[4+i], end, theta + save[i])])
		end = lines[-1][-1]
		theta += save[i]
	return lines

def calc_end(length, start, theta):
	x = length * math.sin(theta)
	y = length * math.cos(theta)
	return (start[0] + x, start[1] + y)

def plotter(pow1, pow2, pow3, length):
	lines = calc_points(pow1, pow2, pow3, length)

	# create the plot
	fig, ax = plt.subplots()

	# add the line segments
	lc = mc.LineCollection(lines, linewidths = 4, color = "darkorange")
	ax.add_collection(lc)

	# add the joint points
	x = [i[0] for j in lines[1:] for i in j]
	y = [i[1] for j in lines[1:] for i in j]
	plt.scatter(x, y, color = "gold")

	# add the top
	plt.plot([-1, length], [0, 0], color = "k")

	# adjust axis shape
	plt.xlim([-1, length])
	plt.ylim([length + 1, -1])
	plt.legend()
	plt.savefig("Spring 2022\Convolutional Model\\test_images\\result_{i}.png".format(i = i + 1))
	plt.show()
	return

for i in range(5):
	plt.close()
	print(results[i])
	plotter(abs(results[i][0] - results[i][3]), abs(results[i][1] - results[i][4]), abs(results[i][2] - results[i][5]), 10)
	