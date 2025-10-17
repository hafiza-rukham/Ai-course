import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"c:\Users\Rukham Ijaz\Downloads\50_Startups (1).csv",delimiter=",")

print(df.head())

print(df.info())
print(df.dtypes)
print(df.describe())
print(df.shape)

import seaborn as sns

variables = ["R&D Spend", "Administration","Marketing Spend"]
for var in variables:
    plt.figure()
    sns.regplot(x=var, y='Profit', data=df).set(title=f'Regression plot of {var} and Profit');
    plt.show()

plt.figure()

correlations = df[["R&D Spend", "Administration","Marketing Spend"]].corr()

print("correlations...\n:" , correlations)

# annot=True displays the correlation values
g = sns.heatmap(correlations, annot=True).set(title='Heat map of Consumption Data - Pearson Correlations')
# Display the plot
plt.show()

y = df['Profit']
X = df[["R&D Spend", "Administration","Marketing Spend"]]

#split the model
SEED = 180
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.10,random_state=SEED)
print(X.shape)

#fit the model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train, y_train)

#print “intercept” 
print("regressor.intercept:", regressor.intercept_)

#And at the coefficients of the features
print("regressor.coef:" , regressor.coef_)

y_pred = regressor.predict(X_test)
print("predict Profile values:")
print(y_pred)

results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(results)

from sklearn.metrics import mean_absolute_error, mean_squared_error
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')