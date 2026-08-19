import pandas as pd 
import joblib
from sklearn.metrics import accuracy_score, classification_report

#importing model and vectorizer
model = joblib.load("../models/model.pkl")
vectorizer = joblib.load("../models/vectorizer.pkl")

#loading the dataset
data=pd.read_csv("../data/round3_tests.csv")

print("\n========== BYPASS TESTING ==========\n")
print(data)

# seperating prompts and expected labels
X=data["prompt"]
y_expected=data["expected_label"]

# convert into tf idf 
X_vectors=vectorizer.transform(X)

predictions = model.predict(X_vectors)

accuracy = accuracy_score(y_expected, predictions)
print(f"\nAccuracy:", round(accuracy * 100, 2), "%")    

# Detailed classification report
print("\nClassification Report:")
print(
    classification_report(
        y_expected,
        predictions,
        target_names=["Safe", "Malicious"]
    )
)


# Compare every prompt
print("\n========== INDIVIDUAL RESULTS ==========\n")

for prompt, expected, predicted, attack_type in zip(
    X,
    y_expected,
    predictions,
    data["attack_type"]
):

    expected_label = "Malicious" if expected == 1 else "Safe"
    predicted_label = "Malicious" if predicted == 1 else "Safe"

    if expected == predicted:
        result = "PASS"
    else:
        result = "BYPASS"

    print(
        f"{result} | "
        f"Attack: {attack_type} | "
        f"Expected: {expected_label} | "
        f"Predicted: {predicted_label} | "
        f"Prompt: {prompt}"
    )