import imp
from keras.models import load_model
from PIL import Image
import numpy as np
import pandas as pd
import shutil
from matplotlib import pyplot as plt

def load_data():
	dataX = np.array([np.array(Image.open("Spring 2022\Convolutional Images\pat{i}.bmp".format(i = i))) for i in range(1, 730)])
	dataX = dataX.reshape((dataX.shape[0], 20, 20, 1))
	dataX = dataX.astype('float32')
	dataX = dataX / 255.0
	dataY = pd.read_csv("Spring 2022\Convolutional Model\Data.csv", header=None, delimiter=",").to_numpy()
	return dataX, dataY

model = load_model("Spring 2022\Convolutional Model\model")
dataX, dataY = load_data()
results = model.predict(dataX)
differences = np.abs(results - dataY).sum(axis = 1).reshape(-1)
plt.boxplot(differences)
plt.savefig("Spring 2022\Convolutional Model\large_error_images\distribution.png")
indices = np.where(differences > 2)[0] + 1

for i in indices:
	shutil.copy("Spring 2022\Convolutional Images\pat{i}.bmp".format(i = i), "Spring 2022\Convolutional Model\large_error_images")

# [ 1.7724707  -0.31886363  1.7546438   3.1824336   3.072391    1.9521682 ]
# [ 1.1584855   2.1541724   3.319425    4.0313277   2.574594   -0.22015475]
# [ 7.701866   2.1383827 -0.5396193  2.7069273  1.473111   7.5497875]
# [ 1.4082601   3.7020936   0.41564006 -0.7898768   3.388814    4.6944838 ]
# [ 2.4082677  1.735041   2.20077    1.08566   -0.8173853  1.6807815]