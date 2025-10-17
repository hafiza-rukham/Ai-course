import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\Rukham Ijaz\Downloads\Documents\GitHub\desktop-tutorial\startup_growth_investment_data.csv", delimiter = ",")
print(df)
print(df.dtypes)

df = df.head(40)
df100 = df.head(30)
print(df)
print(df100)

sns.set_theme(style="whitegrid")

#sns.histplot
s = sns.histplot(data = df,x = "Growth Rate (%)",hue = "Industry")
s.figure.suptitle( "sns.suptitle(data = df,x ='Growth Rate (%)',hue = Industry)")
# Display the plot
s.figure.show()
read = input("Wait for me....")

#sns.Boxplot
s = sns.boxplot(data = df , x = "Industry", y = "Valuation (USD)")
s.figure.suptitle("sns.suptitle(data = df , x = Industry , y = Valuation (USD))")
#Disply the plot
s.figure.show()
read = input("Wait for me....")

#sns.violinplot
s = sns.violinplot(data = df,x = "Industry" , y = "Valuation (USD)")
s.figure.suptitle("sns.violinplot(data = df , x = Industry , y = Valuation (USD))")
#Disply the plot
s.figure.show()
read = input("Wait for me....")

#sns.scatterplot
s = sns.scatterplot(data = df , x = "Funding Rounds", y = "Valuation (USD)", hue = "Industry")
s.figure.suptitle("sns.scatterplot(data = df , x = Funding Rounds, y = Valuation (USD) , hue = 'Industry')")
#Disply the plot
s.figure.show()
read = ("Wait for me....")

#sns.barplot
s = sns.barplot(data = df , x = "Country" , y = "Growth Rate (%)")
s.figure.suptitle("sns.barplot(data = df , x = Country , y = Growth Rate (%))")
#Display the plot
s.figure.show()
read = ("Wait for me.....")

#sns.kdeplot
s = sns.kdeplot(data = df , x = "Industry", y = "Growth Rate (%)")
s.figure.suptitle("sns.kdeplot(data = df , x = Industry , y = Growth Rate (%) )")
#Display the plot
s.figure.show()
read = ("Wait for me....")

#sns.catplot
s = sns.catplot(data = df , x = "Industry", y = "Growth Rate (%)")
s.figure.suptitle("sns.catplot(data = df , x = Industry , y = Growth Rate (%) )")
#Display the plot
s.figure.show()
read = ("Wait for me....")

#.pivot(index="Model", columns="agency", values="price")
pivot = df.pivot(index="Industry", columns="Country", values="Valuation (USD)")

s.figure.heatmap(pivot)
s.figure.suptitle("sns.heatmap(pivot) - pivot = df.pivot(index = Industry, columns=Country, Valuation (USD)")
# Display the plot
s.figure.show()
read = ("Wait for me....")


