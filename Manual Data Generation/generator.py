from functions import *
import numpy as np
import random

def generation(powers):
	generated = np.empty([1, 5])
	for pow1 in powers:
		for pow2 in powers:
			for pow3 in powers:
				pows = [pow1 + (random.random() / 4 - .125), pow2 + (random.random() / 4 - .125), pow3 + (random.random() / 4 - .125)]
				next = list(together(pows[0], pows[1], pows[2], 10))
				generated = np.concatenate((generated, np.array([pows + next])))
	generated = np.delete(generated, 0, 0)
	return generated

availablePowers = [1, 2, 3]
generator = generation(availablePowers)

# generate 540 points
i= 0
while (i < 19):
	generator = np.concatenate((generator, generation(availablePowers)))
	i +=1

np.savetxt("Manual Data Generation/generated_data.csv", generator, delimiter = ",")