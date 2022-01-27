from keras.models import load_model
import pandas as pd

model = load_model("Spring 2022\Model Run\model")
data = None
results = list(model.predict(data))