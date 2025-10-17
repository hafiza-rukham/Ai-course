import pandas as pd
df=pd.read_csv(r"C:\Users\Hajvery Technology\Documents\GitHub\Fullstack-WITH-AI-B-3-SAT-SUN-6Months-Explorer\Week6\student_scores.csv")
print(df)

print(df.head())

print(df.info())
print(df.dtypes)
print(df.describe())
print(df.shape)

df = df.dropna(subset=("Hours","Scores"))

x=df[['Hours']]
y=df[['Scores']]

SEED = 32
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size = 0.3,random_state = SEED)

print(x_train)
print(y_train)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)
print(y_pred)


from sklearn.metrics import mean_absolute_error , mean_squared_error,r2_score

mae = mean_absolute_error(y_test,y_pred)
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'R2 Score: {r2:.2f}')
