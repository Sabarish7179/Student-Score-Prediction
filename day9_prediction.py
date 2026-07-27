import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("clean_student_scores.csv")

# Feature and target
X = data[["Hours"]]
y = data["Score"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict score
hours = [[7]]
prediction = model.predict(hours)

print("Study Hours:", hours[0][0])
print("Predicted Score:", prediction[0])

# Predict multiple values
test_hours = [[2], [4], [6], [8], [10]]
predictions = model.predict(test_hours)

print("\nMultiple Predictions")
for h, score in zip(test_hours, predictions):
    print(f"{h[0]} Hours -> {score:.2f}")