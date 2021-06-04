from keras.layers import Dense, InputLayer, Dropout
from keras.models import Sequential
from keras.callbacks import EarlyStopping
import pandas as pd
from sklearn.model_selection import train_test_split

def create_model():
	model = Sequential()
	# input layer
	model.add(InputLayer(input_shape=(6,)))
	# hidden layers
	model.add(Dense(128, activation = "relu"))
	model.add(Dropout(rate = 0.2))
	model.add(Dense(64, activation = "relu"))
	model.add(Dropout(rate = 0.2))
	model.add(Dense(32, activation = "relu"))
	model.add(Dropout(rate = 0.2))
	# output layer
	model.add(Dense(7))
	model.compile(optimizer = "adam", loss='mse',  metrics=['mae'])
	return model

data = pd.read_csv("pa10_1k.csv", header=None, delimiter="\s+")
features = data.iloc[:, 1:7]
labels = data.iloc[:, 7:14]
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25)

model = create_model()
stop = EarlyStopping(monitor="loss", mode='min', verbose=1, patience=40)
model.fit(features_train, labels_train, epochs = 400, verbose = 1, callbacks=[stop], batch_size=20)
val_mse, val_mae = model.evaluate(features_test, labels_test, verbose = 0)
print(val_mse, val_mae)