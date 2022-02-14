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

# for i in range(1, 10):
# 	im = Image.open("Spring 2022\Convolutional Images\pat{i}.bmp".format(i = i))
# 	# im = im.point(lambda p: 255 if p > 150 else 0)
# 	# im = im.convert("1")
# 	data = np.array(im)
# 	# define subplot
# 	plt.subplot(330 + i)
# 	# plot raw pixel data
# 	plt.imshow(data, cmap=plt.get_cmap('gray'))

# plt.show()

def load_data():
	dataX = np.array([np.array(Image.open("Spring 2022\Convolutional Images\pat{i}.bmp".format(i = i))) for i in range(1, 730)])
	dataX = dataX.reshape((dataX.shape[0], 20, 20, 1))
	dataX = dataX.astype('float32')
	dataX = dataX / 255.0
	dataY = pd.read_csv("Spring 2022\Convolutional Model\Data.csv", header=None, delimiter=",").to_numpy()
	trainX, testX, trainY, testY = train_test_split(dataX, dataY, test_size = 0.2, shuffle = True)
	return trainX, trainY, testX, testY

trainX, trainY, testX, testY = load_data()

# define cnn model
def create_model():
	model = Sequential()
	model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(20, 20, 1)))
	model.add(MaxPooling2D((2, 2)))
	model.add(Flatten())
	model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
	model.add(Dense(6))
	# compile model
	opt = SGD(learning_rate=0.01, momentum=0.9)
	model.compile(optimizer=opt, loss='mse', metrics=['mae'])
	return model

# train the model
def fit_model(model, features, labels, epochs, batch_size):
	stop = EarlyStopping(monitor = "val_loss", mode = "min", verbose = 1, patience = (epochs * 0.1))
	history = model.fit(features, labels, epochs = epochs, verbose = 1, callbacks=[stop], batch_size=batch_size, validation_split = 0.1)
	return history

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

model = create_model()
history = fit_model(model, trainX, trainY, 1500, 25)
plot(history, "Spring 2022\Convolutional Model\model_history.png")
val_mse, val_mae = model.evaluate(testX, testY, verbose = 0)
print(val_mse, val_mae)

model.save("Spring 2022\Convolutional Model\model")
# 0.3280571699142456 0.4047742784023285