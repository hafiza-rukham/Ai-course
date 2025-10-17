import pandas as pd

df = pd.read_csv(r"C:\Users\Rukham Ijaz\OneDrive\Fullstack-WITH-AI-B-3-SAT-SUN-6Months-Explorer\DataSetForPractice\macro_monthly.csv", delimiter=',')
print(df)

print(df.dtypes)
print(df.index)
print(df.describe())
print(df.info())

print(df.to_string())

#Display 5 rows of first
print('first 5 rows')
print(df.head(5))

#display 4 rows of last"
print('last 4 rows')
print(df.tail(4))

#access the name column
Industrial_Production = df['Industrial_Production']
print("access the name column :df :")
print(Industrial_Production)
print()

#access the name column
Manufacturers_New_Orders: Durable Goods = df["Manufacturers_New_Orders: Durable Goods"]
print("access the name column:df :", )
print(Manufacturers_New_Orders: Durable Goods)
print()