import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# -------------------------------
# SECTION 4: DATA ANALYSIS
# -------------------------------

# Filtering
filtered = df[df["score"] > 70]

# Grouping
grouped = df.groupby("course")["score"].mean()

# Sorting
sorted_df = df.sort_values(by="score", ascending=False)

print("Average Score by Course:\n", grouped)

# -------------------------------
# SECTION 5: VISUALIZATION
# -------------------------------

# Bar Chart
df.groupby("course")["score"].mean().plot(kind="bar")
plt.title("Average Score by Course")
plt.xlabel("Course")
plt.ylabel("Score")
plt.show()

# Line Chart
df["score"].plot(kind="line")
plt.title("Score Trend")
plt.xlabel("Index")
plt.ylabel("Score")
plt.show()

# -------------------------------
# PROBABILITY
# -------------------------------

total_students = len(df)
passed_students = len(df[df["score"] >= 40])  # assuming pass >= 40

probability = passed_students / total_students

print(f"\nProbability of Passing: {probability} ({probability*100:.2f}%)")