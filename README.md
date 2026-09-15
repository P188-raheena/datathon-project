# 🩺 Diabetes Prediction Using Machine Learning

A Machine Learning web application that predicts whether a person is likely to have diabetes based on selected medical parameters.

The application uses a **Logistic Regression** model trained on the **PIMA Indians Diabetes Dataset** and provides predictions through a simple **Flask web interface**.

> ⚠️ **Educational Project:** This application is intended for learning and demonstration purposes. It is not a medical diagnostic tool.

---

## 📌 Project Overview

Diabetes is a common chronic health condition. Machine Learning can be used to analyze medical data and identify patterns that may help predict the likelihood of diabetes.

This project demonstrates a complete basic Machine Learning workflow:

1. Load the diabetes dataset
2. Separate features and target
3. Split the data into training and testing sets
4. Scale the input features using `StandardScaler`
5. Train a Logistic Regression model
6. Evaluate the model
7. Save the trained model and scaler
8. Build a Flask web application
9. Accept user input through an HTML form
10. Generate and display a prediction

---

## 🎯 Objective

The main objective of this project is to build a simple Machine Learning application that can:

- Accept medical parameters from a user
- Process the input data
- Use a trained Machine Learning model
- Predict the possibility of diabetes
- Display the prediction result
- Display a prediction confidence score

---

## 🚀 Features

- 🖥️ Simple and user-friendly web interface
- 🤖 Machine Learning-based prediction
- 📊 Logistic Regression classification model
- ⚙️ Feature scaling using `StandardScaler`
- 🔮 Real-time prediction through Flask
- 📈 Prediction confidence score
- 🎨 HTML and CSS frontend
- 🐍 Python-based backend
- 📁 Pre-trained model files included
- 🔄 Model can be retrained using the provided training script

---

## 🧠 Machine Learning Workflow

The project follows this workflow:

```text
                Diabetes Dataset
                       │
                       ▼
              Data Preprocessing
                       │
                       ▼
              Train/Test Split
                       │
                       ▼
                StandardScaler
                       │
                       ▼
             Logistic Regression
                       │
                       ▼
                 Model Training
                       │
                       ▼
                Model Evaluation
                       │
                       ▼
          diabetes_model.pkl
                 + scaler.pkl
                       │
                       ▼
                Flask Application
                       │
                       ▼
                 User Input Form
                       │
                       ▼
                  Prediction
                       │
                       ▼
             Prediction Result
```

---

## 📊 Input Features

The model uses the following medical parameters:

| Feature | Description |
|---|---|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| Blood Pressure | Diastolic blood pressure |
| Skin Thickness | Triceps skin fold thickness |
| Insulin | Serum insulin level |
| BMI | Body Mass Index |
| Diabetes Pedigree Function | Diabetes-related family history score |
| Age | Age of the person |

### Prediction Output

The model predicts one of two classes:

```text
0 → Non-Diabetic
1 → Diabetic
```

---

## 📂 Dataset

### Dataset Used

**PIMA Indians Diabetes Dataset**

The dataset contains medical measurements used to predict whether a person has diabetes.

The target column is:

```text
Outcome
```

Where:

```text
0 = Non-Diabetic
1 = Diabetic
```

The dataset is included in this repository as:

```text
diabetes.csv
```

---

## 🤖 Machine Learning Model

### Algorithm

The project uses:

**Logistic Regression**

Logistic Regression is a classification algorithm suitable for predicting one of two possible outcomes.

### Preprocessing

Before training the model, the input features are standardized using:

```python
StandardScaler()
```

### Train/Test Split

The dataset is divided into:

- **80% Training Data**
- **20% Testing Data**

The training script uses a fixed random state to make the result reproducible.

---

## 📈 Model Performance

The current training run produced:

**Test Accuracy: 71%**

The project also calculates:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

Model performance can vary depending on the dataset and training configuration.

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Logistic Regression
- StandardScaler

### Data Processing

- Pandas
- NumPy

### Backend

- Flask

### Frontend

- HTML5
- CSS3

### Model Storage

- Pickle

### Development Tool

- Visual Studio Code

---

## 📁 Project Structure

```text
datathon-project/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── train_model.py
├── diabetes.csv
├── diabetes_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

### File Description

| File/Folder | Purpose |
|---|---|
| `app.py` | Flask application and prediction logic |
| `train_model.py` | Trains and evaluates the Machine Learning model |
| `diabetes.csv` | Dataset used for training |
| `diabetes_model.pkl` | Saved trained Logistic Regression model |
| `scaler.pkl` | Saved StandardScaler |
| `templates/` | Contains HTML pages |
| `index.html` | User input page |
| `result.html` | Prediction result page |
| `static/` | Contains static files |
| `style.css` | Styling for the web application |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

# ⚙️ Installation

## 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/P188-raheena/datathon-project.git
```

---

## 2. Move Into the Project Folder

```bash
cd datathon-project
```

---

## 3. Install Required Libraries

Install the dependencies using:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

## Step 1 — Train the Model

If you want to retrain the Machine Learning model, run:

```bash
python train_model.py
```

This creates:

```text
diabetes_model.pkl
scaler.pkl
```

You only need to retrain the model if you want to create new model files.

---

## Step 2 — Start the Flask Application

Run:

```bash
python app.py
```

You should see:

```text
Running on http://127.0.0.1:5000
```

---

## Step 3 — Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🖥️ How to Use the Application

### Step 1

Open the application in your browser.

### Step 2

Enter the required medical parameters.

### Step 3

Click the **Predict** button.

### Step 4

The application processes the input through the trained Machine Learning model.

### Step 5

The result page displays:

- Prediction result
- Prediction confidence
- Message related to the prediction

Example:

```text
Prediction Result

Diabetic

Prediction Confidence: 89.74%
```

---

# 🔄 Retraining the Model

To train the model again using the dataset:

```bash
python train_model.py
```

The script:

1. Loads `diabetes.csv`
2. Checks the dataset
3. Separates features and target
4. Splits the data
5. Scales the features
6. Trains Logistic Regression
7. Evaluates the model
8. Saves the trained model
9. Saves the scaler
10. Performs a sample prediction

Generated files:

```text
diabetes_model.pkl
scaler.pkl
```

---

# 📷 Screenshots

## Home Page

_Add your application homepage screenshot here._

## Input Form

_Add your input form screenshot here._

## Prediction Result

_Add your prediction result screenshot here._

Example:

```text
Prediction Result
-------------------------
Diabetic
Prediction Confidence: 89.74%
```

---

# 🔮 Future Enhancements

The project can be improved by adding:

- Random Forest classification
- XGBoost
- Hyperparameter tuning
- Cross-validation
- Better handling of missing or invalid values
- More detailed data visualization
- Explainable AI using SHAP
- Patient history
- User authentication
- Doctor dashboard
- Database integration
- Cloud deployment
- REST API
- Mobile application

---

# ⚠️ Disclaimer

This project is created for **educational and demonstration purposes only**.

The predictions generated by this application **should not be considered a medical diagnosis** and should not be used for making medical decisions.

If you have concerns about diabetes or your health, please consult a qualified healthcare professional.

---

# 👩‍💻 Author

**Raheena P**

B.Tech Computer Science Engineering Student

Interested in:

- Software Development
- Machine Learning
- Artificial Intelligence
- Data Science

---

# 📜 License

This project is created for educational and academic purposes.

---

## ⭐ Support

If you find this project useful for learning Machine Learning and Flask, consider giving the repository a ⭐ star.
