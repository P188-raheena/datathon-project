from flask import Flask, render_template, request
import numpy as np
import pickle

# ===============================
# Create Flask App
# ===============================
app = Flask(__name__)

# ===============================
# Load Trained Model
# ===============================
model = pickle.load(open("diabetes_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ===============================
# Home Page
# ===============================
@app.route("/")
def home():
    return render_template("index.html")


# ===============================
# Prediction Route
# ===============================
@app.route("/predict", methods=["POST"])
def predict():

    try:
        pregnancies = float(request.form["Pregnancies"])
        glucose = float(request.form["Glucose"])
        blood_pressure = float(request.form["BloodPressure"])
        skin_thickness = float(request.form["SkinThickness"])
        insulin = float(request.form["Insulin"])
        bmi = float(request.form["BMI"])
        dpf = float(request.form["DiabetesPedigreeFunction"])
        age = float(request.form["Age"])

        features = np.array([
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            dpf,
            age
        ]).reshape(1, -1)

        # Scale Input
        features = scaler.transform(features)

        # Prediction
        prediction = model.predict(features)[0]

        # Probability
        probability = model.predict_proba(features)[0][prediction] * 100

        if prediction == 1:
            result = "Diabetic"
            color = "red"
            message = "The patient is likely to have diabetes. Please consult a healthcare professional."
        else:
            result = "Non-Diabetic"
            color = "green"
            message = "The patient is unlikely to have diabetes. Continue maintaining a healthy lifestyle."

        return render_template(
            "result.html",
            prediction=result,
            probability=round(probability, 2),
            color=color,
            message=message
        )

    except Exception as e:
        return render_template(
            "result.html",
            prediction="Error",
            probability=0,
            color="orange",
            message=str(e)
        )


# ===============================
# Run App
# ===============================
if __name__ == "__main__":
    app.run(debug=True)
