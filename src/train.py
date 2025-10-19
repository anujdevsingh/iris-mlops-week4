from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd, joblib, json, os

os.makedirs("data", exist_ok=True)
os.makedirs("model", exist_ok=True)

iris = load_iris(as_frame=True)
df = iris.frame
df.to_csv("data/iris.csv", index=False)

X, y = df.drop(columns=["target"]), df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)

acc = accuracy_score(y_test, pred)
joblib.dump(model, "model/model.pkl")
json.dump({"accuracy": acc}, open("model/metrics.json", "w"))
print(f"✅ Model trained. Accuracy = {acc:.3f}")
