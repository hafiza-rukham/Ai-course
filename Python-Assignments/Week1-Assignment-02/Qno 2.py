# Assignment 1: Write a program, to list all words, with vowel in it.
vowel_list = ["Humanity", "Artificial" ,"Silence", 
    "Parameters", "Council" , "Intelligence" ]
print("list of Vowel words:", vowel_list)

#Assignment 2: Write a program , to have “List” , with all “noun” in story. Print them.
noun_list = ["Human", "Freedom", 
            "City", "Dr.Elies Voss"]
print("List of noun words:", noun_list)

#Assignment 2b: Write a program , to have “List” , with all “noun” in story. Last Element should a nested List, with 
#Numbers in story. Print them.
noun_list = ["Human", "Freedom", 
            "City", "Dr.Elies Voss"]
number = [9,1]
noun_list.append(number)
print(noun_list)

#Assignment 3:Write a program , to have “Tuples” , with all “noun” in story.
my_tuple = ("Athena-9", "Global", "hesitation")
print("Noun words:", my_tuple)

#Assignment 3b:Write a program , to have “Tuples” , with all “noun” in story. Print them. Last Element should a nested 
#Tuples, with Numbers in story. Print them. 
my_tuple = ("Athena-9", "Global", "hesitation")
print("Noun words:", my_tuple)
number = (10,4)
my_tuple = my_tuple + (number,)
print(my_tuple)

#Assignment 4: Write a program , to have “Sets” , with all noun in story. Print them. . Last Element should a nested Sets, 
#with Numbers in story. Print them.
my_set = {"Scientist", "Air", "hands", 
          "screens", "silence"} 
print("noun words;", my_set)
#sets are mutable so they cant be inside another set 
#so we use ferozenset() to make it immutable
num = {9,1}
nested_num = frozenset(num)
my_set.add(nested_num)
print(my_set)

#Assignment 5: Write a program , to have “Dictionaries” , with all noun in story. Print them. Last Element should a 
#nested Dictionaries, with Numbers in story. Print them.
my_dictionary = {"Air":1,"hesitation":2,"Global":3,
"screens":4 , "Human":5}
print("noun words:", my_dictionary)
numbers = {"Numbers": {10: "ten", 1: "one"}}
my_dictionary.update(numbers)
print(my_dictionary)