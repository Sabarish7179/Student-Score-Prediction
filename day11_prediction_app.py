import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("clean_student_scores.csv")

# Feature and Target
X = data[["Hours"]]
y = data["Score"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# User input
hours = float(input("Enter Study Hours: "))

# Prediction
prediction = model.predict([[hours]])

print("--------------------------------")
print("Study Hours:", hours)
print("Predicted Score:", round(prediction[0], 2))
print("--------------------------------")