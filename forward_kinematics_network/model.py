from keras.layers import Dense, InputLayer, Dropout
from keras.models import Sequential
from keras.callbacks import EarlyStopping
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

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

def create_model():
	model = Sequential()
	# input layer
	model.add(InputLayer(input_shape=(6,)))
	# hidden layers
	model.add(Dense(128, activation = "relu"))
	model.add(Dropout(rate = 0.05))
	model.add(Dense(64, activation = "relu"))
	model.add(Dropout(rate = 0.05))
	model.add(Dense(32, activation = "relu"))
	# output layer
	model.add(Dense(7))
	model.compile(optimizer = "adam", loss='mse',  metrics=['mae'])
	return model

def fit_model(model, features, labels, epochs, batch_size):
	stop = EarlyStopping(monitor = "val_loss", mode = "min", verbose = 1, patience = (epochs * 0.1))
	history = model.fit(features, labels, epochs = epochs, verbose = 1, callbacks=[stop], batch_size=batch_size, validation_split = 0.1)
	return history

data = pd.read_csv("pa10_config000_50k.csv", header=None, delimiter="\s+")
features = data.iloc[:, 1:7]
labels = data.iloc[:, 7:14]
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25)

model = create_model()
history = fit_model(model, features_train, labels_train, 1500, 750)
plot(history, "forwards_kinematics_network/model_history.png")
val_mse, val_mae = model.evaluate(features_test, labels_test, verbose = 0)
print(val_mse, val_mae)

model.save_weights("network")