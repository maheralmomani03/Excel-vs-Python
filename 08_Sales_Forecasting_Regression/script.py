import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Load historical sales data from Excel Table
df = xl("Forecast_Table[#All]", headers=True)

# 2. Prepare data for the model (X: Month, y: Sales)
X = df[['Month']]
y = df['Sales']

# 3. Train the Linear Regression model
model = LinearRegression().fit(X, y)

# 4. Predict sales for the next period (Month 7)
next_month = [[7]]
prediction = model.predict(next_month)

# Output formatted result
f"Predicted Sales (Month 7): {prediction[0]:,.2f}"