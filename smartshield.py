# SmartShield-Lite
# AI Based Network Intrusion Detection System

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = {
    "packet_size": [120, 300, 450, 600, 50, 900, 200, 700],
    "duration": [1, 2, 3, 5, 0.5, 6, 1.5, 4],
    "failed_logins": [0, 1, 0, 2, 0, 3, 1, 2],
    "attack": [0, 0, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df.drop("attack", axis=1)
y = df["attack"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)
