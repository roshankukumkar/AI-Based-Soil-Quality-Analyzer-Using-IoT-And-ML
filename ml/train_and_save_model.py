import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load updated dataset (with soil_moisture)
df = pd.read_csv("../dataset/Crop_recommendation (1).csv")

# Feature order MUST match dataset exactly
X = df[[
    "N",
    "P",
    "K",
    "temperature",
    "humidity",
    "soil_moisture",
    "ph",
    "rainfall"
]]

y = df["label"]

# Encode labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# Strong RandomForest (no scaling needed)
model = RandomForestClassifier(
    n_estimators=500,
    random_state=42
)

model.fit(X_train, y_train)

# Accuracy check
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("🎯 Accuracy:", round(accuracy * 100, 2), "%")

# Save model & encoder
with open("crop_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)

print("✅ Model trained and saved successfully!")