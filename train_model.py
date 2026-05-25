import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# LOAD DATASET
data = pd.read_csv("dataset/resume_dataset_200k_enhanced.csv")

# SELECT INPUT FEATURES
X = data[[
    'cgpa',
    'internships',
    'projects',
    'experience_years',
    'hackathons',
    'research_papers',
    'skills_score',
    'soft_skills_score',
    'resume_length_words'
]]

# TARGET OUTPUT
y = data['hired']

# SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# MODEL
model = RandomForestClassifier()

# TRAIN MODEL
model.fit(X_train, y_train)

# PREDICTION
y_pred = model.predict(X_test)

# ACCURACY
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# SAVE MODEL
joblib.dump(model, "hiring_model.pkl")

print("Hiring Prediction Model Saved Successfully")