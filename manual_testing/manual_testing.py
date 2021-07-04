import pandas as pd
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt

# Forward model testing

actual = pd.read_csv("manual_testing/Book1.csv", header = None)
manual = actual.iloc[:, :6]
forward = load_model("forward_kinematics_network/network")

results = list(forward.predict(manual))
forward_predicted = pd.DataFrame(np.vstack(results))
forward_predicted.to_csv("manual_testing/forward_predicted.csv")

# given = pd.read_csv("manual_testing/Data exploration.csv", header = None)

def plot_forward(manual, predicted, given = None):
	'''
	Plots the forward model's predictions against the calculated results
	'''
	fig, (ax1, ax2) = plt.subplots(1, 2)
	x1 = manual[6].tolist()
	z1 = manual[8].tolist()
	x2 = predicted[0].tolist()
	z2 = predicted[2].tolist()
	y1 = manual[7].tolist()
	y2 = predicted[1].tolist()
	ax1.plot(x1, z1, label = "Actual")
	ax1.plot(x2, z2, label = "Predicted")
	ax2.plot(y1, z1, label = "Actual")
	ax2.plot(y2, z2, label = "Predicted")
	if given != None:
		x3 = given[0].tolist()
		y3 = given[1].tolist()
		z3 = given[2].tolist()
		ax2.plot(y3, z3, label = "Given")
		ax1.plot(x3, z3, label = "Given")
	ax1.set(xlabel = "X-Value", ylabel = "Z-Value")
	ax2.set(xlabel = "Y-Value", xlim = [-1, 1])
	plt.legend()
	plt.savefig("manual_testing/foward_comparison.png")
	return ax1, ax2

# plot_forward(manual, forward_predicted)

# Inverse model testing

manual = pd.read_csv("manual_testing/forward_predicted.csv")
manual = manual.iloc[:, 1:]
inverse = load_model("inverse_kinematics_network/network")

results = list(inverse.predict(manual))
inverse_predicted = pd.DataFrame(np.vstack(results))
inverse_predicted.to_csv("manual_testing/inverse_predicted.csv")

def plot_inverse_motors(actual, predicted):
	'''
	Plots the inverse model's predictions against the actual values
	'''
	fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(1, 6)
	x = range(151)
	y1 = predicted[0].tolist()
	y12 = actual[0].tolist()
	y2 = predicted[1].tolist()
	y22 = actual[1].tolist()
	y3 = predicted[2].tolist()
	y32 = actual[2].tolist()
	y4 = predicted[3].tolist()
	y42 = actual[3].tolist()
	y5 = predicted[4].tolist()
	y52 = actual[4].tolist()
	y6 = predicted[5].tolist()
	y62 = actual[5].tolist()
	ax1.plot(x, y1, label = "Predicted")
	ax1.plot(x, y12, label = "Actual")
	ax2.plot(x, y2, label = "Predicted")
	ax2.plot(x, y22, label = "Actual")
	ax3.plot(x, y3, label = "Predicted")
	ax3.plot(x, y32, label = "Actual")
	ax4.plot(x, y4, label = "Predicted")
	ax4.plot(x, y42, label = "Actual")
	ax5.plot(x, y5, label = "Predicted")
	ax5.plot(x, y52, label = "Actual")
	ax6.plot(x, y6, label = "Predicted")
	ax6.plot(x, y62, label = "Actual")
	ax1.set(xlabel = "Motor 1", ylabel = "Radians", ylim = [-2, 2])
	ax2.set(xlabel = "Motor 2", ylim = [-2, 2])
	ax3.set(xlabel = "Motor 3", ylim = [-2, 2])
	ax4.set(xlabel = "Motor 4", ylim = [-2, 2])
	ax5.set(xlabel = "Motor 5", ylim = [-2, 2])
	ax6.set(xlabel = "Motor 6", ylim = [-2, 2])
	plt.legend()
	plt.savefig("manual_testing/inverse_comparison.png")
	return
# plot_inverse_motors(actual, inverse_predicted)

def forward_inverse_forward(manual, forward_predicted, inverse_predicted):
	''' Plot forward -> inverse -> forward
	'''
	ax1, ax2 = plot_forward(manual, forward_predicted)
	results = list(forward.predict(inverse_predicted))
	forward_again = pd.DataFrame(np.vstack(results))
	forward_again.to_csv("manual_testing/forward_inverse_forward_predicted.csv")
	x = forward_again[0].tolist()
	y = forward_again[1].tolist()
	z = forward_again[2].tolist()
	ax1.plot(x, z, label = "Inverse")
	ax2.plot(y, z, label = "Inverse")
	plt.savefig("manual_testing/forward_inverse_forward_comparison.png")
	return

forward_inverse_forward(actual, forward_predicted, inverse_predicted)
plt.show()