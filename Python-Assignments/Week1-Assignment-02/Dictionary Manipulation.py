my_dictionary = {
    'Jhon': 23,
    'Charlie': 20, 
    'Henry': 25,
    'Peter': 30}

#Check if a value exists in a dictionary
key_check = ("Henry")
if key_check in my_dictionary.keys():
    print(my_dictionary[key_check])

# Get the key of a minimum value from the following dictionary
min_key = min(my_dictionary, key=my_dictionary.get)
print(min_key)

#Delete a list of keys from a dictionary
keys_to_delete = ['Charlie','Peter']
for key in keys_to_delete:
    my_dictionary.pop(key,None)  
    print(my_dictionary)