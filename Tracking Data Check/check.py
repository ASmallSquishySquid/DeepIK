import joblib

with open("Tracking Data Check/pos10t5.pkl", "rb") as file:
	data = joblib.load(file)
print(data["default"][0])

