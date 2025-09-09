from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(_name_)

# Model load karo (maan lo aapne model.pkl banaya hai training ke baad)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "🚗 Welcome to Car Price Prediction!"

@app.route("/predict", methods=["POST"])
def predict():
    # User input lete hain
    data = request.get_json()
    features = np.array(list(data.values())).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": float(prediction[0])}

if _name_ == "_main_":
    app.run(debug=True)
