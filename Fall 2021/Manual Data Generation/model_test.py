import pandas as pd
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
from functions import *
import math
import random

# calculate loss on normal points and make comparisons for non-normal points

# plot robot path

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

def plotter(expected_x, expected_y, pow1, pow2, pow3, length):
	lines = calc_points(pow1, pow2, pow3, length)

	# create the plot
	fig, ax = plt.subplots()

	# add the expected endpoint
	plt.scatter([expected_x], [expected_y], color = "r", s = 50, label = "Expected endpoint")

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
	plt.savefig("Manual Data Generation/comparison.png")
	plt.show()
	return

index = random.randint(0, 49)
manual = pd.read_csv("Manual Data Generation\manual_data.csv", header = None).iloc[index : index + 1, :]
model = load_model("Manual Data Generation\model")
results = model.predict(manual.iloc[:, 3:])

expected_x = manual.iat[0, 3]
expected_y = manual.iat[0, 4]

# results = model.predict(np.array([(7.5, 2.5)]))
# expected_x = 7.5
# expected_y = 2.5

plotter(expected_x, expected_y, results[0][0], results[0][1], results[0][2], 10)