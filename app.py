from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Flask app banate hain
app = Flask(__name__)

# Model load karna (maan lo aapne model.pkl banaya hai)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "✅ Car Price Prediction API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()  # frontend ya API se input lena

    # Example: data = {"year": 2015, "present_price": 5.59, "kms_driven": 27000, "owner": 0, "fuel_type": "Petrol"}
    year = data["year"]
    present_price = data["present_price"]
    kms_driven = data["kms_driven"]
    owner = data["owner"]
    fuel_type = 1 if data["fuel_type"] == "Petrol" else 0  # Simple encoding

    input_data = np.array([[year, present_price, kms_driven, owner, fuel_type]])
    prediction = model.predict(input_data)[0]

    return jsonify({"Predicted Price": round(prediction, 2)})

if _name_ == "_main_":
    import os
    port = int( os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)
    app.run(debug=True)


import os
print("Current Working Directory:", os.getcwd())
