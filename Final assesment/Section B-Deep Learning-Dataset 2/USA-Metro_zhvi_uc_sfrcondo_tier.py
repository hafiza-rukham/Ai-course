#In this project, we predict monthly home prices (ZHVI: Zillow Home Value Index) for a specific metro area in the 
# USA — here, New York, NY.We use Long Short-Term Memory (LSTM) neural networks, a type of Recurrent Neural Network (RNN), 
# suitable for time series forecasting because it can capture long-term dependencies in sequential data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from keras.metrics import Precision, Recall

df = pd.read_csv(r"C:\Users\Hajvery Technology\Documents\GitHub\Ai-course\USA-Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv")
print(df.head())

print(df.info())
print(df.dtypes)
print(df.describe())
print(df.shape)

# Select one metro
metro_name = "New York, NY"
data = df[df["RegionName"] == metro_name]

# Drop non-date columns
meta_cols = ["RegionID", "SizeRank", "RegionName", "RegionType", "StateName"]
data = data.drop(columns=meta_cols)

# transpose: dates to rows
series = data.T
series.index = pd.to_datetime(series.index)
series.columns = ["price"]

# Convert wide to single time series
values = series["price"].values.reshape(-1, 1)
dates = series.index

#scaling
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(values)

# Create sliding windows
window_size = 12
X = []
y = []

for i in range(window_size, len(scaled_data)):
    X.append(scaled_data[i - window_size:i])
    y.append(scaled_data[i])

X = np.array(X)
y = np.array(y)

#Train-test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,  test_size=0.2, shuffle=False
)

X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

#Build LSTM Model
model = Sequential()
model.add(LSTM(units=128, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=128))
model.add(Dropout(0.2))
model.add(Dense(1))

model.compile(
    optimizer='adam',
    loss='mean_squared_error',
    metrics=['mae']
)

#Training and Evaluating the Model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1)

predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions).flatten()
y_test = scaler.inverse_transform(y_test.reshape(-1,1)).flatten()

rmse = np.sqrt(np.mean((y_test - predictions)**2))
print(f'RMSE: {rmse:.2f}')

# Visualization
plt.figure(figsize=(12,6))
plt.plot(dates[-len(y_test):], y_test, label='Actual Prices')
plt.plot(dates[-len(predictions):], predictions, label='Predicted Prices')
plt.title(f'Actual vs Predicted Home Prices ({metro_name})')
plt.xlabel('Date')
plt.ylabel('ZHVI Home Value')
plt.legend()
plt.show()

input("wait")

# in this model graph
# Blue line: Actual home prices in New York
# Orange line: LSTM model ki predicted prices


#Conclusion & Analysis
# Model Performance:
# RMSE = 48,382 USD → shows prediction error scale
# MAE values during training were low → good fit
# Observations:
# Model captures trends and seasonality of home prices
# Some months show small deviations → could improve with more data or feature engineering
# Future Improvements:
# Include macroeconomic indicators (interest rates, unemployment)
# Hyperparameter tuning (LSTM units, layers, epochs)
# Test with other metro areas