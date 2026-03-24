import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset
df = pd.read_csv("students.csv")

# Features & Target
X = df[["hours_studied"]]
y = df["score"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, pred)
rmse = mse ** 0.5

print("RMSE:", rmse)

# Sample prediction
sample = pd.DataFrame([[5]], columns=["hours_studied"])
prediction = model.predict(sample)

print("Predicted score for 5 hours study:", prediction[0])