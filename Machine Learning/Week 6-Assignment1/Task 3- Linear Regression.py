import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Rukham Ijaz\Downloads\number-of-registered-medical-and-dental-doctors-by-gender-in-pakistan (1).csv",delimiter=",",index_col="Years")

print(df.head())

df.info()
print(df.dtypes)
print(df.describe())
print(df.shape)

X = df['Female Doctors'].values.reshape(-1, 1)
y = df['Female Dentists'].values.reshape(-1, 1)

print(X.shape)
print(y.shape)

#So, what's the relationship between these variables? A great way to explore relationships between variables is through Scatter plots. We'll plot the hours on the X-axis and scores on the Y-axis, and for each pair, a marker will be positioned based on their values:
df.plot.scatter(x='Female Doctors', y='Female Dentists', title='Scatter Plot of Female Doctors and Female Dentists percentages');
plt.show()

SEED = 40

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = SEED)

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
def calc(slope, intercept, Female_Doctors):
    return (slope*Female_Doctors)+intercept

Female_Dentists = calc(regressor.coef_, regressor.intercept_, 8.3)
print(Female_Dentists)

#pridict “Female Doctors’ for testing data based on testing data for “Female Doctors”
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

