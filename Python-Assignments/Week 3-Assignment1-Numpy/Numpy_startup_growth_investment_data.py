import numpy as np

catplot,Number_of_Investors = np.genfromtxt(r"C:\Users\Rukham Ijaz\Downloads\Documents\GitHub\desktop-tutorial\startup_growth_investment_data.csv",delimiter=',', usecols=(3,5), unpack=True, dtype=None,skip_header=1)

print(catplot)
print(Number_of_Investors)

#Statistic operation
print("catplot mean:",np.mean(catplot))
print("catplot median:",np.median(catplot))
print("catplot std:",np.std(catplot))
print("catplot average:",np.average(catplot))
print("catplot percentile - 25:",np.percentile(catplot,25))
print("catplot percentile - 75:",np.percentile(catplot,75))
print("catplot min:",np.min(catplot))
print("catplot max:",np.max(catplot))

#Math operation 
print("catplot square:",np.square(catplot))
print("catplot sqrt:", np.sqrt(catplot))
print("catplot power:",np.sqrt(catplot))
print("catplot abs:",np.abs(catplot))

#Perform basic arithmatic operation
addition = catplot + Number_of_Investors
substraction = catplot - Number_of_Investors
multiplication = catplot * Number_of_Investors
division = catplot / Number_of_Investors

print("calculate addition:",addition)
print("calculate substraction:",substraction)
print("calculate multiplication:",multiplication)
print("calculate division:",division)

#Trignometric functions
catplotPie = (catplot/np.pi) +1
sin_values = np.sin(catplotPie)
cosine_values = np.cos(catplotPie)
tangent_values = np.tan(catplotPie)

print("catplot -div -pie - sin values:",sin_values)
print("catplot -div -pie - cosine values:",cosine_values)
print("catplot -div -pie - tangent values:",tangent_values)

#Calculate the natural logarithm and 10-base logarithm
log_array = np.log(catplotPie)
log10_array = np.log10(catplotPie)

print("catplot -div -pie - natural logarithm:",log_array)
print("catplot -div -pie - 10-Base logarithm:",log10_array) 

# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(catplotPie)
print("catplot -div -pie -hyperbolic sine:",sinh_values)

# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(catplotPie)
print("catplot - div -pie -cosh_values:",cosh_values)

# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(catplotPie)
print("catplot - div - pie -tanh_values:",tanh_values)

#Calculate the inverse hyperbolic sine of each element
asinh_values = np.arccosh(catplotPie)
print("catplot - div -pie -Inverse Hyperbolic sine values:",asinh_values)

#Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(catplotPie)
print("catplot - div -pie -inverse Hyperbolic cosine values:",acosh_values)

#2Dimension array
D2catplotNumberofinvester = np.array([catplot,Number_of_Investors])
print("catplot plus number of invester - 2Dimension array:",D2catplotNumberofinvester)

# check the dimension of array1
print("catplot plus number of invester - 2Dimension array - dimension:",D2catplotNumberofinvester.ndim)

# return total number of elements in array1
print("catplot plus number of invester - 2Dimension array - total number of elements:",D2catplotNumberofinvester.shape)

# return a tuple that gives size of array in each dimension
print("catplot plus number of invester - 2Dimension array - gives size of array in ech element:",D2catplotNumberofinvester.size)

# check the data type of array1
print("catplot plus number of invester - 2Dimension array -data type:",D2catplotNumberofinvester.dtype)

# Splicing array
D2catplotNumberofinvesterslice = D2catplotNumberofinvester[:2:6]
print("catplot Plus number of invester - 2 dimentional arrary - Splicing array - D2LongLat[:2,:6] " , D2catplotNumberofinvesterslice)

# Indexing array
D2catplotNumberofinvestersliceitemonly = D2catplotNumberofinvester[5:4:1]
print("catplot plus number of invester - 2Dimension array - index array- D2catplotNumberofinvester:",D2catplotNumberofinvestersliceitemonly)

#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2catplotNumberofinvester):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2catplotNumberofinvester):
    print(index, elem)

print()