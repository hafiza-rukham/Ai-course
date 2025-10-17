import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\Hajvery Technology\Downloads\housing.csv",delimiter=",")

print(df.head())

print(df.info())
print(df.dtypes)
print(df.describe())
print(df.shape)

x = df[[""]]
df = df.dropna(subset=())