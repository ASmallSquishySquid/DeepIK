import joblib
import matplotlib.pyplot as plt
import numpy as np
import random

for f in range(10, 16):
	with open("Tracking Data Check/Run {f}/pos{f}t5.pkl".format(f = f), "rb") as file:
		data = joblib.load(file)

	for i in range(10):
		img = random.randrange(729)
		check = np.array(data["default"][img])
		x, y = check.T

		plt.plot(x, y)
		plt.axis("equal")
		plt.gca().invert_yaxis()
		plt.savefig("Tracking Data Check/Run {f}/check{img}.png".format(img = img, f = f))
		plt.cla()