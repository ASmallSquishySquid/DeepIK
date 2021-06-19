import pandas as pd
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt

manual = pd.read_csv("manual_testing/Book1.csv", header = None)
manual_features = manual.iloc[:, :6]
manual_labels = manual.iloc[:, 6:]
model = load_model("forward_kinematics_network/network")

# val_mse, val_mae = model.evaluate(manual_features, manual_labels, verbose = 0)
# print(val_mse, val_mae)

results = list(model.predict(manual_features))
predicted = pd.DataFrame(np.vstack(results))
predicted.to_csv("manual_testing/forward_predicted.csv")

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
ax1.set(xlabel = "X-Value", ylabel = "Z-Value")
ax2.set(xlabel = "Y-Value")
plt.legend()
plt.savefig("manual_testing/foward_comparison.png")
plt.show()