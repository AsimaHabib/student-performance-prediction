
import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression

# Training data: [study_hours, prev_score]
X = np.array([
    [1, 40],
    [2, 45],
    [3, 50],
    [4, 60],
    [5, 65],
    [6, 70],
    [7, 75],
    [8, 85],
    [2, 80],
    [1, 30]
])

# 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1, 0])

# Train the model
model = LogisticRegression()
model.fit(X, y)

# Save the trained model
joblib.dump(model, "model.pkl")

print("Model trained and saved to model.pkl")

# Test on training data
predictions = model.predict(X)
print("Sample predictions:", predictions)
print("Actual labels:     ", y)
