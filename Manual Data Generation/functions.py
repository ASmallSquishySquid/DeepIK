import math

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

def independent(theta1, theta2, theta3, length1, length2, length3, length4):
	x = length2 * math.sin(theta1) + length3 * math.sin(theta1 + theta2) + length4 * math.sin(theta1 + theta2 + theta3)
	y = length1 + length2 * math.cos(theta1) + length3 * math.cos(theta1 + theta2) + length4 * math.cos(theta1 + theta2 + theta3)
	return x, y

def together(p1, p2, p3, length):
	theta1, theta2, theta3, length1, length2, length3, length4 = dependent(p1, p2, p3, length)
	return independent(theta1, theta2, theta3, length1, length2, length3, length4)