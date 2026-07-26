import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ==========================
# Load Dataset
# ==========================
dataset = pd.read_csv("diabetes.csv")

print("First 5 Rows")
print(dataset.head())

print("\nDataset Shape:", dataset.shape)

print("\nMissing Values")
print(dataset.isnull().sum())

# ==========================
# Features and Target
# ==========================

X = dataset.drop("Outcome", axis=1)
Y = dataset["Outcome"]

# ==========================
# Train Test Split
# ==========================

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.20,
    random_state=42,
    stratify=Y
)

# ==========================
# Feature Scaling
# ==========================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ==========================
# Model Training
# ==========================

model = LogisticRegression(max_iter=1000)

model.fit(X_train, Y_train)

# ==========================
# Model Evaluation
# ==========================

train_prediction = model.predict(X_train)
test_prediction = model.predict(X_test)

train_accuracy = accuracy_score(Y_train, train_prediction)
test_accuracy = accuracy_score(Y_test, test_prediction)

print("\nTraining Accuracy :", round(train_accuracy * 100, 2), "%")
print("Testing Accuracy  :", round(test_accuracy * 100, 2), "%")

print("\nConfusion Matrix")
print(confusion_matrix(Y_test, test_prediction))

print("\nClassification Report")
print(classification_report(Y_test, test_prediction))

# ==========================
# Save Model
# ==========================

with open("diabetes_model.pkl", "wb") as file:
    pickle.dump(model, file)

with open("scaler.pkl", "wb") as file:
    pickle.dump(scaler, file)

print("\nModel Saved Successfully")
print("Files Created:")
print("1. diabetes_model.pkl")
print("2. scaler.pkl")

# ==========================
# Sample Prediction
# ==========================

sample = [[6,148,72,35,0,33.6,0.627,50]]

sample = scaler.transform(sample)

prediction = model.predict(sample)

if prediction[0] == 0:
    print("\nPrediction : Non-Diabetic")
else:
    print("\nPrediction : Diabetic")
