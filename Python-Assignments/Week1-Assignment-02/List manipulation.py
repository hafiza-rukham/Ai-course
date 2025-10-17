#Reverse a lisi in Python
my_list = ["Rumail",12,5.3,True]
print(my_list)
my_list.reverse()
print("Reverse a list:",my_list) 

#Turn every item of a list into its square 
my_list = [2,4,6,8,10]
my_list = [x**2 for x in my_list]
print("turn every item of a list into its square:",my_list)

# Remove empty strings from the list of strings 
a = ["Rumail","","Rukham","Mahnoor",""]
print(a)
a = [item for item in a if item != ""]
print(a)

# Add new item to list after a specified item
my_list2 = [29,"april",2005,"Rukham"]
print(my_list2)
my_list2.insert(1,20)
print("after insert(20):",my_list2)

#Replace list’s item with new value if found
my_list2 = [29,"april",2005,"Rukham"]
old_value = "april"
new_value = "may"
for i in range(len(my_list2)):
    if my_list2[i] == old_value:
        my_list2[i] = new_value
print(my_list2) 