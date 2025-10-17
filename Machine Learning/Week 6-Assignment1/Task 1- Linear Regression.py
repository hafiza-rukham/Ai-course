import pandas as pd
import matplotlib.pyplot as plt

url = "https://github.com/ShahzadSarwar10/FULLSTACK-WITH-AI-BOOTCAMP-B1-MonToFri-2.5Month-Explorer/raw/main/DataSetForPractice/Real_Estate_Sales_2001-2022_GL-Short.csv"
df = pd.read_csv(url,index_col="Serial Number")

print(df.head())

df.info()
print(df.dtypes)
print(df.describe())
print(df.shape)

X = df['Assessed Value'].values.reshape(-1, 1)
y = df['Sale Amount'].values.reshape(-1, 1)

print(X.shape)
print(y.shape)

#So, what's the relationship between these variables? A great way to explore relationships between variables is through Scatter plots. We'll plot the hours on the X-axis and scores on the Y-axis, and for each pair, a marker will be positioned based on their values:
df.plot.scatter(x='Assessed Value', y='Sale Amount', title='Scatter Plot of Sale Amount and Assessed Value percentages');
plt.show()

SEED = 40

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = SEED)

print(X_train)
print(y_train)

#Training a Linear Regression Model

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
 
#fit the model
regressor.fit(X_train, y_train)
print(regressor.intercept_)

#For retrieving the slope (which is also the coefficient of x):

print(regressor.coef_)

#python function to calculate “price’ based on  “bedrooms” - with “intercept” and “slope” 
def calc(slope, intercept, Assessed_Value):
    return (slope*Assessed_Value)+intercept

Sale_Value = calc(regressor.coef_, regressor.intercept_, 9.5)
print(Sale_Value)

#pridict “Sale Amount’ for testing data based on testing data for “Assessed Value”
y_pred = regressor.predict(X_test)
df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)

from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')