import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from a CSV file
df = pd.read_csv(r"C:\Users\Rukham Ijaz\OneDrive\Documents\GitHub\Projects\RealEstate-USA.csv", delimiter=',',parse_dates=[11],date_format={'date_time':'%d-%m-%y'},index_col='brokered_by')
print(df)

print(df.info())
print(df.dtypes)
print(df.describe())
print(df.shape)

df = df.head(20)
df100 = df.head(30)
print(df)
print(df100)

sns.set_theme(style ='darkgrid')

# Line Plot, with X parameter – as  “city“ and y parameter as “price” 
s = sns.lineplot(data=df,x = "city", y = "price")
s.figure.suptitle("sns.lineplot(data = df , x = city, y = price)")
# Display the plot
s.figure.show()
read = input("Wait for me....")

#categorical plots, with X parameter – as  “city “ and y parameter as “price” 
s = sns.catplot(data=df , x = "city", y = "price")
s.figure.suptitle("sns.catplot(data = df , x = 'city', y = 'price')")
# Display the plot
s.figure.show()
read = input("Wait for me....")

# Plot univariate or bivariate distributions using kernel density estimation, with X parameter – 
# as  “zip_code“ and y parameter as “price” 
s = sns.kdeplot( data = df,x = "zip_code",y = "price" )
s.figure.suptitle("sns.kdeplot(data = df, x = zip_code, y = price)")
# Display the plot
s.figure.show()
read = input("Wait for me....")

#scatter plot, with X parameter – as  “zip_code“ and y parameter as “price”
s = sns.scatterplot(data = df,x ="zip_code",y="price")
s.figure.suptitle("sns.scatterplot(data= df ,x = zip_code, y = price)")
#Display the plot
s.figure.show()
read = input("Wait for me....")

# bar plot, with X parameter – as  “zip_code“ and y parameter as “price” t
s = sns.barplot(data = df, x = "zip_code",y = "price")
s.figure.suptitle("sns.barplot(data = df,x = price , y = acre_lot)")
# Display the plot
s.figure.show()
read = input("Wait for me.... ")

# Plot rectangular data as a color-encoded matrix, with X parameter – as  “zip_code“ and y parameter as “price” 
var = df.pivot(index = "price", columns= "zipcode", values = "acre_lot")

s = sns.heatmap(var)
s.figure.suptitle("sns.heatmap(var) - var = df.pivot(index = price, columns = zipcode , values= acre_lot)")
#Display the plot
s.figure.show()
read = input("Wait for me....")

# Draw - Plot univariate or bivariate distributions using kernel density estimation
s = sns.kdeplot(data = df , x = "zip_code", y = "price")
s.fifure.suptitle("sns.kdeplot(data = df ,x = zipcode , y = price)")
#Display the plot
s.figure.show()
read = input("Wait for me....")

#- Line Plot, with X parameter – as  “zip_code“ and y parameter as “price” 
s = sns.lineplot(data=df, x = "zip_code", y = "price")
s.figures.suptitle("sns.lineplot(data = df,x = zip_code, y = price)")
#display the plot
s.figure.show()
read = input("Wair for me....")

#categorical plots, with X parameter – as  “zip_code“ and y parameter as “price” 
s = sns.catplot(data = df,x = "zip_code", y = "price")
s.figure.suptitle("data = df, x = zip_code, y = price")
#display the plot
s.figure.show()
read = input("Wait for me....")

#bar plot, with X parameter – as  “City“ and y parameter as “Price” 
s = sns.barplot(data =  df, x = "city", y = "price")
s.figure.suptitle("data = df, x = city, y = price")
#display the plot
s.figure.show()
read = ("Wait for me....")

#Plot rectangular data as a color-encoded matrix, with X parameter – as  “City“ and 
# y parameter as “Price” 
var = df.pivot(index = "price",columns="city",values="acre_lot")
s.figure.suptitle("index = price,columns = city, values =acre_lot ")
#display the plot
s.figure.show()
read = ("Wait for me....")

# Plot univariate or bivariate distributions using kernel density estimation, with X 
# parameter – as  “City“ and y parameter as “Price” 
s = sns.kdeplot( data = df,x = "city",y = "price" )
s.figure.suptitle("sns.kdeplot(data = df, x = city, y = price)")
# Display the plot
s.figure.show()
read = input("Wait for me....")

#scatter plot, with X parameter – as  “City“ and y parameter as “Price”
s = sns.scatterplot(data = df,x ="city",y="price")
s.figure.suptitle("sns.scatterplot(data= df ,x = city, y = price)")
#Display the plot
s.figure.show()
read = input("Wait for me....")

# Line Plot,  to create as with X parameter – as  “year“ and y parameter as “Price”
s = sns.lineplot(data=df,x = "year", y = "price")
s.figure.suptitle("sns.lineplot(data = df , x = year, y = price)")
# Display the plot
s.figure.show()
read = input("Wait for me....")

# categorical plots,  to create as with X parameter – as  “year“  and y parameter as “Price” 
s = sns.catplot(data = df,x = "year", y = "price")
s.figure.suptitle("data = df, x = year, y = price")
#display the plot
s.figure.show()
read = input("Wait for me....")

#Plot univariate or bivariate distributions using kernel density estimation,  to create as 
# with X parameter – as  “year“  and y parameter as “Price” 
s = sns.kdeplot( data = df,x = "year",y = "price" )
s.figure.suptitle("sns.kdeplot(data = df, x = year, y = price)")
# Display the plot
s.figure.show()
read = input("Wait for me....")

#scatter plot, with  to create as with X parameter – as  “year“  and y parameter as “Price”
s = sns.scatterplot(data = df,x ="year",y="price")
s.figure.suptitle("sns.scatterplot(data= df ,x = year, y = price)")
#Display the plot
s.figure.show()
read = input("Wait for me....")

#bar plot, with  to create as with X parameter – as  “year“  and y parameter as “Price”
s = sns.barplot(data =  df, x = "year", y = "price")
s.figure.suptitle("data = df, x = year, y = price")
#display the plot
s.figure.show()
read = ("Wait for me....")

# Plot rectangular data as a color-encoded matrix, with  to create as with X parameter – as  
# “year“ and y parameter as “Price” 
var = df.pivot(index = "price",columns="year",values="acre_lot")
s.figure.suptitle("index = price,columns = year, values =acre_lot ")
#display the plot
s.figure.show()
read = ("Wait for me....")

#line plot, set following 5 theme one by one. [sns.set_theme( ) ] 
# Create a plot
sns.lineplot(x='city', y='price', data=df)
plt.show()

# Other themes can be set similarly
sns.set_theme(style='whitegrid')
sns.lineplot(x='city', y='price', data=df)
plt.show()

sns.set_theme(style='dark')
sns.lineplot(x='city', y='price', data=df)
plt.show()

sns.set_theme(style='white')
sns.lineplot(x='city', y='price', data=df)
plt.show()

sns.set_theme(style='ticks')
sns.lineplot(x='city', y='price', data=df)
plt.show()

#Bar plot, set following 5 theme one by one. [sns.set_style( ) ] 
# Create a plot
sns.barplotplot(x='city', y='price', data=df)
plt.show()

# Other themes can be set similarly
sns.set_theme(style='whitegrid')
sns.barplot(x='city', y='price', data=df)
plt.show()

sns.set_theme(style='dark')
sns.barplot(x='city', y='price', data=df)
plt.show()

sns.set_theme(style='white')
sns.barplot(x='city', y='price', data=df)
plt.show()

sns.set_theme(style='ticks')
sns.barplot(x='city', y='price', data=df)
plt.show()

