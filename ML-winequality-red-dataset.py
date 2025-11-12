import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\Hajvery Technology\\Documents\\GitHub\\Ai-course\\winequality-red[1].csv",delimiter=";")
print(df)

# Display info
print(df.info())
# print description
print(df.describe())
#Head
print(df.head())
#Tail
print(df.tail())

import seaborn as sns
variables = ["free sulfur dioxide","volatile acidity","citric acid","residual sugar","fixed acidity","density","pH","sulphates","alcohol"]
for var in variables:
    sns.regplot(x=var,y='quality', data = df)
    plt.show()

read = input("Wait here: \n")


x = df[["free sulfur dioxide","volatile acidity","citric acid","residual sugar","fixed acidity","density","pH","sulphates","alcohol"]]
y = df[["quality"]]

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(x)
x_scaler=scaler.transform(x.values)
print(x_scaler)

#split
SEED = 42
from sklearn.model_selection import train_test_split
x_train_scaler, x_test_train, y_train,y_test = train_test_split(x_scaler,y , train_size=.2,random_state=SEED)

print(x_train_scaler)
print(y_train)

#fit
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train_scaler,y_train)

#predict
y_pred = regressor.predict(x_test_train)
print(y_pred)

from sklearn.metrics import mean_absolute_error , mean_squared_error,r2_score

mae = mean_absolute_error(y_test,y_pred)
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'R2 Score: {r2:.2f}')

