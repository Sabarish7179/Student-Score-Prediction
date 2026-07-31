import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = pd.read_csv("Data/clean_student_scores.csv")

print(data.head())
# Input (Feature)
X = data[["Hours"]]

# Output (Target)
y = data["Score"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)

print("Model trained successfully!")
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)
