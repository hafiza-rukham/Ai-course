import pandas as pd

df = pd.read_csv(r"C:\Users\Rukham Ijaz\OneDrive\Documents\GitHub\projects\RealEstate-USA.csv", delimiter=',',parse_dates=[11],date_format={'date_time':'%d-%m-%y'})
print(df)

print(df.dtypes)
print(df.index)
print(df.describe())
print(df.info())

#Display 9 rows of first
print('first 9 rows')
print(df.head(9))

#display 9 rows of last"
print('last 9 rows')
print(df.tail(9))

#access the name column
city = df['city']
print("access the name column :df :")
print(city)
print()

#access the name column
street = df['street']
print("access the name column :df :")
print(street)
print()

#access multiple column
street_city= df [["street","city"]]
print("access multiple column")
print(street_city)
print()

#Selecting a single row using .loc
row = df.loc[5]
print("Selecting a single row using . loc:",row)
print(row)
print()

#Selecting multiple row using .loc
row1 = df.loc[[3,5,7]]
print("Selecting multiple row using .loc:",row1)
print(row1)
print()

#Selecting a slice of rows using .loc
row2 = df.loc[3:9]
print("Selecting a slice of rows using .loc:",row2)
print(row2)
print()

print(df['price'].unique())

#Conditional selection of rows using .loc
row3 = df.loc[df['price'] > 100000]
print("Conditional selection of rows using .loc:",row3)
print(row3)
print()

#Conditional selection of rows using .loc
row4 = df.loc[df['city'] == "Puerto Rice" ]
print("Conditional selection of rows using .loc:",row3)
print(row4)
print()

#Conditional selection of rows using .loc
row5 = df.loc[df["price"] <= 180500 ]
print("conditional selection of rows using .loc:", row3)
print(row5)
print()

#selecting a single column using .loc
row6 = df.loc[:7,'price']
print("selecting a single column using .loc" )
print(row6)
print()

#selecting a slice of column using .loc
row7 = df.loc[:1,'city':'zip_code']
print("selecting a slice of column using .loc")
print(row7)
print()

#Combined row and column selection using .loc
row8 = df.loc[df['city'] == "Adjuntas",'city':'zip_code']
print("combined row and column selection using .loc ")
print(row8)
print()

#selecting a single row using  . iloc
row = df.iloc[4]
print("selecting a single row using .iloc")
print(row)
print()

#selecting multiple rows using . iloc
row1 = df.iloc[[6,8,14]]
print("Selecting multiple rows using.iloc")
print(row1)
print()

#selecting a slice of rows using .iloc
row2 = df.iloc[4:12]
print("selecting a slice of rows using .iloc")
print(row2)
print()

#Selecting a single column using .iloc 
col3 = df.iloc[:2]
print("Selecting a single column using .iloc ")
print(col3)
print()

#Selecting multiple columns using .iloc 
col4 = df.iloc[[1,3,6]]
print("selecting multiple columns using iloc")
print(col3)
print()

#Selecting a slice of columns using .iloc
col4 = df.iloc[:,1:5]
print("selecting a slice of columns using iloc")
print(col4)
print()

# Combined row and column selection using .iloc 
col4 = df.iloc[[6,8,14],[1,3]]
print("combined rows and columns using iloc")
print(col4)
print()

# Combined row and column selection using .iloc 
col5 = df.iloc[[1,5],[1,3]]
print(" Combined row and column selection using .iloc ")
print(col5)
print()

#Add a New Row to a Pandas DataFrame
df.loc[len(df.index)] = [1678, "for_sale",239001,8,4,0.32,1661558,"Arecibo","Puerto Rico",612,2756,None]
print("Modified DataFrame - add a new row:")
print(df)
print()

# delete row with index 2
df.drop(index=2, inplace=True)
# delete rows with index 4 and 7
df.drop([4, 7], axis=0, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame - Remove Rows:")
print(df)

#delete house_size and state columns
df.drop(["house_size","state"], axis=1 , inplace=True)
print("Modified DataFrame -  delete house_size ,state :")
print(df)

#Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
df.rename(columns= {"state" : "state_changed"}, inplace=True)
print("Modified DataFrame  - Rename Labels :")
print(df)

#Rename label from 3 to 5
df.rename(index={3:5}, inplace=True)
print("Modified DataFrame  - Rename Labels :")
print(df)

#query() to Select Data
selected_rows = df.query('city == \'Adjuntas\' or price < 127400 ')
print(selected_rows.to_string())
print(len(selected_rows))

# sort DataFrame by price in ascending order
sorted_df = df.sort_values(by="price")
print(sorted_df.to_string(index=False))

# group the DataFrame by the 'city' column and calculate the sum of 'price' for each category
grouped = df.groupby("city")["price"].sum()
print(grouped.to_string())
print("grouped :", len(grouped))

#use dropna() to remove rows with any missing values
cleaned_df = df.dropna()
print("Cleaned Data:\n",cleaned_df)

# filling NaN values with 0
df.fillna(0, inplace=True)
print("filling NaN values with 0:", df)