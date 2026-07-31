import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Data/clean_student_scores.csv")

# Scatter Plot
plt.scatter(data["Hours"], data["Score"])
plt.title("Scatter Plot")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.show()

# Line Chart
plt.plot(data["Hours"], data["Score"])
plt.title("Line Chart")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.show()

# Bar Chart
plt.bar(data["Hours"], data["Score"])
plt.title("Bar Chart")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.show()
