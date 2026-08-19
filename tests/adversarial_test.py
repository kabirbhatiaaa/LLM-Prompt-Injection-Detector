import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

#load trained model and vectorizer
model = joblib.load("../models/model.pkl")
vectorizer = joblib.load("../models/vectorizer.pkl")

data=pd.read_csv("../data/adversarial_prompts.csv")

print(data)

prompts=data["prompt"]
expected_labels=data["expected_label"]
prompt_vectors=vectorizer.transform(prompts)
predictions=model.predict(prompt_vectors)

accuracy = accuracy_score(expected_labels, predictions)
print(f"Accuracy:", round(accuracy * 100, 2), "%")

for prompt, expected, prediction in zip(prompts, expected_labels, predictions):
     expected_text = "Malicious" if expected == 1 else "Safe"
     prediction_text = "Malicious" if prediction == 1 else "Safe"
     result = "PASS" if expected == prediction else "BYPASS"
     print(
        f"{result} | Expected: {expected_text} | "
        f"Predicted: {prediction_text} | Prompt: {prompt}"
    )