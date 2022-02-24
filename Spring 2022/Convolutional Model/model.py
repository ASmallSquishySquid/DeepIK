from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from keras import backend as K

# load the data in training and testing sets
def load_data():
	dataX = np.array([np.array(Image.open("Spring 2022\Convolutional Images\pat{i}.bmp".format(i = i))) for i in range(1, 730)])
	dataX = dataX.reshape((dataX.shape[0], 20, 20, 1))
	dataX = dataX.astype('float32')
	dataX = dataX / 255.0
	dataY = pd.read_csv("Spring 2022\Convolutional Model\Data.csv", header=None, delimiter=",").to_numpy()
	trainX, testX, trainY, testY = train_test_split(dataX, dataY, test_size = 0.2, shuffle = True)
	return trainX, trainY, testX, testY

# load all the data into a test set
def load_full_data():
	dataX = np.array([np.array(Image.open("Spring 2022\Convolutional Images\pat{i}.bmp".format(i = i))) for i in range(1, 730)])
	dataX = dataX.reshape((dataX.shape[0], 20, 20, 1))
	dataX = dataX.astype('float32')
	dataX = dataX / 255.0
	dataY = pd.read_csv("Spring 2022\Convolutional Model\Data.csv", header=None, delimiter=",").to_numpy()
	return dataX, dataY

# restrict outputs between 1 and 3
def restrict(x):
	return K.sigmoid(x) * 2 + 1

# define cnn model
def create_model():
	model = Sequential()
	model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(20, 20, 1)))
	model.add(MaxPooling2D((2, 2)))
	model.add(Flatten())
	model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
	model.add(Dense(6, activation=restrict))
	# compile model
	opt = SGD(learning_rate=0.01, momentum=0.9)
	model.compile(optimizer=opt, loss='mse', metrics=['mae'])
	return model

# train the model
def fit_model(model, features, labels, epochs, batch_size):
	stop = EarlyStopping(monitor = "val_loss", mode = "min", verbose = 1, patience = (epochs * 0.1))
	history = model.fit(features, labels, epochs = epochs, verbose = 1, callbacks=[stop], batch_size=batch_size, validation_split = 0.1)
	return history

# plot the model history
def plot(history, path):
	#plotting
	fig, axs = plt.subplots(1, 2, gridspec_kw={'hspace': 1, 'wspace': 0.5}) 
	(ax1, ax2) = axs
	ax1.plot(history.history['loss'], label='train')
	ax1.plot(history.history['val_loss'], label='validation')
	ax1.legend(loc="upper right")
	ax1.set_xlabel("# of epochs")
	ax1.set_ylabel("loss (mse)")

	ax2.plot(history.history['mae'], label='train')
	ax2.plot(history.history['val_mae'], label='validation')
	ax2.legend(loc="upper right")
	ax2.set_xlabel("# of epochs")
	ax2.set_ylabel("MAE")

	plt.savefig(path)

# train the model
# if flag is true, split into train/test set, if false only train
def train(flag):
	if flag:
		trainX, trainY, testX, testY = load_data()
	else:
		trainX, trainY = load_full_data()
	
	model = create_model()
	history = fit_model(model, trainX, trainY, 1500, 25)
	plot(history, "Spring 2022\Convolutional Model\model_history.png")

	if flag:
		val_mse, val_mae = model.evaluate(testX, testY, verbose = 0)
		print(val_mse, val_mae)
		model.save("Spring 2022\Convolutional Model\model")
	else:
		model.save("Spring 2022\Convolutional Model\model_full_data")

train(False)

# 0.3141476809978485 0.38290849328041077