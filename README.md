# 🩺 Diabetes Prediction Using Machine Learning

A Machine Learning web application that predicts whether a person is diabetic based on medical parameters. The application uses a Logistic Regression model trained on the PIMA Indians Diabetes Dataset and provides real-time predictions through a Flask web interface.

---

## 📌 Project Overview

Diabetes is one of the most common chronic diseases worldwide. Early detection can help patients receive timely treatment and reduce complications.

This project predicts the likelihood of diabetes using patient medical data such as:

- Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin
- Body Mass Index (BMI)
- Diabetes Pedigree Function
- Age

The trained Machine Learning model predicts whether the patient is:

- ✅ Non-Diabetic
- ❌ Diabetic

---

# 🚀 Features

- User-friendly web interface
- Machine Learning prediction
- Logistic Regression algorithm
- Data preprocessing using StandardScaler
- Real-time prediction
- Prediction confidence score
- Responsive design
- Easy deployment using Flask

---

# 🛠 Technologies Used

## Programming Language

- Python

## Machine Learning

- Scikit-learn

## Libraries

- Pandas
- NumPy
- Pickle

## Frontend

- HTML5
- CSS3

## Backend

- Flask

## IDE

- Visual Studio Code

---

# 📂 Project Structure

```
Diabetes-Prediction-ML/
│
├── app.py
├── train_model.py
├── diabetes.csv
├── diabetes_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
│
├── templates/
│      ├── index.html
│      └── result.html
│
├── static/
│      └── style.css
```

---

# 📊 Dataset

Dataset Used:

**PIMA Indians Diabetes Dataset**

Features:

- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age

Target:

Outcome

- 0 → Non-Diabetic
- 1 → Diabetic

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Diabetes-Prediction-ML.git
```

Move into the project folder

```bash
cd Diabetes-Prediction-ML
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

### Step 1

Train the model

```bash
python train_model.py
```

### Step 2

Run Flask

```bash
python app.py
```

### Step 3

Open

```
http://127.0.0.1:5000
```

---

# 📈 Model Used

Algorithm:

- Logistic Regression

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Expected Accuracy:

**78%–82%**

---

# 📷 Screenshots

Add screenshots here:

- Home Page
- Input Form
- Prediction Result
- Accuracy Graph

---

# 🔮 Future Enhancements

- Random Forest Model
- XGBoost
- Deep Learning
- Doctor Dashboard
- Patient History
- Cloud Deployment
- Mobile Application
- Explainable AI (SHAP)

---

# 👨‍💻 Author

**Raheena P**

B.Tech Student

Machine Learning Enthusiast

---

# 📜 License

This project is created for educational and academic purposes.

---

⭐ If you like this project, don't forget to star the repository.
