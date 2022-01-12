import joblib
import matplotlib.pyplot as plt
import numpy as np
import random

with open("Tracking Data Check/pos10t5.pkl", "rb") as file:
	data = joblib.load(file)

for i in range(4):
	img = random.randrange(729)
	check = np.array(data["default"][img])
	x, y = check.T

	plt.plot(x, y)
	plt.axis("equal")
	plt.savefig("Tracking Data Check/check{img}.png".format(img = img))
	plt.show()