from keras.models import load_model
from PIL import Image
import numpy as np
import pandas as pd
import shutil
from matplotlib import pyplot as plt
from os import scandir

def load_data():
	dataX = np.array([np.array(Image.open(file.path)) for file in scandir("Spring 2022\Convolutional Images") if file.name.endswith(".bmp")])
	dataX = dataX.reshape((dataX.shape[0], 35, 35, 1))
	dataX = dataX.astype('float32')
	dataX = dataX / 255.0
	dataY = pd.read_csv("Spring 2022\Convolutional Model\\NewData.csv", header=None, delimiter=",").to_numpy()
	return dataX, dataY

def get_outliers(model, move):
	model = load_model("Spring 2022\Convolutional Model\{model}".format(model = model))
	dataX, dataY = load_data()
	results = model.predict(dataX)
	differences = np.abs(results - dataY).sum(axis = 1).reshape(-1)
	plt.boxplot(differences)
	plt.savefig("Spring 2022\Convolutional Model\{move}\distribution.png".format(move = move))
	cutoff = 1.5 * np.subtract(*np.percentile(differences, [75, 25])) + np.percentile(differences, 75)
	indices = np.where(differences > cutoff)[0] + 1
	print(len(indices))
	for i in indices:
		shutil.copy("Spring 2022\Convolutional Images\pat{i}t=16.bmp".format(i = i), "Spring 2022\Convolutional Model\{move}".format(move = move))
	if len(indices) != 0:
		print(model.predict(dataX[indices - 1]))

get_outliers("model_full_data", "large_error_images")

# no restrictions
# [ 1.7724707  -0.31886363  1.7546438   3.1824336   3.072391    1.9521682 ]
# [ 1.1584855   2.1541724   3.319425    4.0313277   2.574594   -0.22015475]
# [ 7.701866   2.1383827 -0.5396193  2.7069273  1.473111   7.5497875]
# [ 1.4082601   3.7020936   0.41564006 -0.7898768   3.388814    4.6944838 ]
# [ 2.4082677  1.735041   2.20077    1.08566   -0.8173853  1.6807815]

# no restrictions, full data set
#  [ 1.2232714   0.16957247  1.771165    0.75968504  3.4326816  -0.3207851 ]
#  [ 0.675837    0.33842638  1.8376062   1.7062995   2.3252215  -1.0393219 ]
#  [ 6.3082724   1.0577066   1.7608283   1.5605059  -3.7371697   8.600754  ]
#  [ 1.930093    3.6137955   1.4817257  -1.1728753  -0.71463954  4.296635  ]
#  [ 0.63360906  0.76397663  2.0132444   1.1663606   0.7888966  -0.6583449 ]

# restricted output
#  [1.0341141 1.043922  1.009026  1.0856221 2.9999983 1.0025772]
#  [1.0000062 1.1554368 2.7617774 2.999952  2.9890757 1.0000099]
#  [3.        2.3841937 1.0001197 1.0001069 1.0163506 3.       ]
#  [1.0532708 2.9989266 1.31023   1.        2.9999876 3.       ]
#  [1.000093  1.0761931 1.7196306 2.128115  2.8741689 1.0233731]

# restricted output, full data set
#  [1.0524147 1.0050917 1.773076  2.9882221 2.9476979 1.8055156]
#  [1.002445  1.2304412 2.8938022 2.997885  2.5146317 1.073456 ]
#  [2.9999964 1.0001299 1.0605073 1.0001109 1.3965042 3.       ]
#  [1.0304326 2.9716232 1.3840804 1.        2.0455222 3.       ]
#  [1.0000045 1.2251207 2.2985058 2.973017  2.0582044 1.1232069]