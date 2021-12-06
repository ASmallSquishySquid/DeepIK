from functions import *
import numpy as np
import random

# generate data for training
def generation(start, stop, points):
	generated = np.empty([1, 5])
	for i in range(points):
		pow1 = random.uniform(start, stop)
		for j in range(points):
			pow2 = random.uniform(start, stop)
			for k in range(points):
				pow3 = random.uniform(start, stop)
				pows = [pow1, pow2, pow3]
				pos = list(together(pows[0], pows[1], pows[2], 10))
				generated = np.concatenate((generated, np.array([pows + pos])))
	generated = np.delete(generated, 0, 0)
	return generated

# generator = generation(0.5, 3.5, 3)

# # generate 540 points
# i= 0
# while (i < 19):
# 	generator = np.concatenate((generator, generation(0.5, 3.5, 3)))
# 	i += 1

# np.savetxt("Manual Data Generation/generated_data.csv", generator, delimiter = ",")

def manual_generation(start, stop):
	pow1 = random.uniform(start, stop)
	pow2 = random.uniform(start, stop)
	pow3 = random.uniform(start, stop)
	pows = [pow1, pow2, pow3]
	pos = list(together(pows[0], pows[1], pows[2], 10))
	return np.array([pows + pos])

# generate 50 datapoints for manual testing
generator = manual_generation(1, 3)
for i in range(49):
	generator = np.concatenate((generator, manual_generation(1, 3)))

np.savetxt("Manual Data Generation/manual_data.csv", generator, delimiter = ",")