#Write a program to create a new string made of an input string’s first, 
# middle, and last character.
text = input("Enter string:")
first_character= text[0]
middle_character = text[len(text)//2]
last_character = text[-1]
new_string = first_character + middle_character + last_character
print("New string:",new_string)

#Write a program to count occurrences of all characters within a string Given.
str = "I am Pakistani"
char_count = {}
for ch in str:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1
print(char_count)

#Reverse a given string 
str = "I am Pakistani"
reversed_str = str[::-1]
print(reversed_str)

#Split a string on hyphens 
str = "I-am-Pakistani"
parts = str.split("-")
print(parts)

#Remove special symbols / punctuation from a string
import string
text = "Hello! How's everything?"
cleaned_text = ''.join([char for char in text if char not in string.punctuation])
print(cleaned_text)