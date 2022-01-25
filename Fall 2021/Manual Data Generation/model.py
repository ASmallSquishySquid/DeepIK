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
	model.add(InputLayer(input_shape=(2,)))
	# hidden layers
	model.add(Dense(128, activation = "relu"))
	model.add(Dropout(rate = 0.05))
	model.add(Dense(64, activation = "relu"))
	model.add(Dropout(rate = 0.05))
	model.add(Dense(16, activation = "relu"))
	# output layer
	model.add(Dense(3))
	model.compile(optimizer = "adam", loss='mse',  metrics=['mae'])
	return model

def fit_model(model, features, labels, epochs, batch_size):
	stop = EarlyStopping(monitor = "val_loss", mode = "min", verbose = 1, patience = (epochs * 0.1))
	history = model.fit(features, labels, epochs = epochs, verbose = 1, callbacks=[stop], batch_size=batch_size, validation_split = 0.1)
	return history

data = pd.read_csv("Manual Data Generation\generated_data.csv", header=None, delimiter=",")
labels_train = data.iloc[:-40, 0:3]
features_train = data.iloc[:-40, 3:]
labels_test = data.iloc[-40:, 0:3]
features_test = data.iloc[-40:, 3:]
# features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25)

# train the inverse model
model = create_model()
history = fit_model(model, features_train, labels_train, 1500, 50)
plot(history, "Manual Data Generation/model_history.png")
val_mse, val_mae = model.evaluate(features_test, labels_test, verbose = 0)
print(val_mse, val_mae)

model.save("Manual Data Generation/model")
# 0.5643492937088013 0.6222490072250366