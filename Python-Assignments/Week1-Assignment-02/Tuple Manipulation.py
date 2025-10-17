my_tuple = (1,2,3,4,5)

#Reverse the tuple
my_tuple = tuple(reversed(my_tuple)) 
print(my_tuple)

#Access value 20 from the tuple
my_tuple = (10,20,30,40,50)
value = my_tuple[1]
print(value)

#Swap two tuples in Python 
tuple1 = (2,4,6,8)
tuple2 = (3,6,9,12)

print("before swaping : tuple1 = {tuple1}, tuple2 = {tuple2}")
#swap the tuple
tuple1, tuple2 = tuple2 , tuple2
print("after swaping : tuple1 = {tuple2}, tuple2 = {tuple1}")