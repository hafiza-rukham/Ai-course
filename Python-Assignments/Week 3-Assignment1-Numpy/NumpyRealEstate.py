import numpy as np

price, house_size ,brokered_by ,acre_lot ,city = np.genfromtxt(r"C:\Users\Rukham Ijaz\OneDrive\Documents\GitHub\Projects\Numpy\RealEstate-USA.csv", delimiter=',',usecols=(0,2,5,7,10), unpack=True,dtype=None,skip_header=1,invalid_raise=False)

print(house_size)
print(price)
print(brokered_by)
print(acre_lot)
print(city)

#Perform Statistic operation on array of "Price"
print("Real Estate price mean:" , np.mean(price))
print("Real Estate price average:" , np.average(price))
print("Real Estate price median:" , np.median(price))
print("Real Estate price max:" , np.max(price))
print("Real Estate price min:" , np.min(price))
print("Real Estate price  percentile - 25:" ,np.percentile(price,25))
print("Real Estate price  percentile - 75:" ,np.percentile(price,75))

#Perform Statistic operation on array of "house_size"
print("house_size mean:" , np.mean(house_size))
print("house_size average:" ,np.average(house_size))
print("Real Estate price median:" ,np.median(house_size))
print("Real Estate price  max:" ,np.max(house_size))
print("Real Estate price  min:" ,np.min(house_size))
print("Real Estate price  percentile - 25:" ,np.percentile(house_size,25))
print("Real Estate price  percentile - 75:" ,np.percentile(house_size,75))

#Math operation
print("price square:",np.square(price))
print("price sqrt:",np.sqrt(price))
print("price power:",np.power(price,price))
print("price abs:",np.abs(price))

#perform basic arrithmatic operations
addition = price + house_size
subtraction = price - house_size
multiplication = price * house_size
division = price / house_size

print("calculate addition:,",addition)
print("calculate subtraction:",subtraction)
print("calculate multiplication:",multiplication)
print("calculate division:",division)

#Trignometric function
pricePie = (price/np.pi) +1
sin_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)

print("price -div -pie - sin values:",sin_values)
print("price - div - pie - cosine values:", cosine_values)
print("price - div - pie - tangent values:",tangent_values)

#calculate the natural logarithm and base_10 logarithm
log_array = np.log(pricePie)
log10_array = np.log10(pricePie)

print("price - div - pie - natural logarithm values:",log_array)
print("price - div - pie - base 10 logarithm values:",log10_array)

# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(pricePie)
print("price - div - pie - hyperbolic sine :",sinh_values)

# Calculate the hyperbolic cosh() of each element
cosh_values = np.cosh(pricePie)
print("price - div - pie - hyperbolic cosine values:",cosh_values)

#calculate the hyperbolic tangent of each element
tanh_values = np.tanh(pricePie)
print("price - div - pie - hyperbolic tangent values:",tanh_values)

#calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(pricePie)
print("price - div - pie - inverse hyperbolic sine values:",asinh_values)

#calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(pricePie)
print("price - div - pie - inverse hyperbolic cosine values:",acosh_values)

#2 dimension array
D2house_sizeprice = np.array([house_size,price])
print("price plus size - 2 dimension array:",D2house_sizeprice)
print("price plus size - 2 dimension array- dimension:",D2house_sizeprice.ndim)
print("price plus size - 2 dimension array-total number of element:",D2house_sizeprice.size)
print("price plus size - 2 dimension array -give siza of array in each dimension:",D2house_sizeprice.shape)
print("price plus size - 2 dimension array - data type:",D2house_sizeprice.dtype)

#3 dimension array
d3_array = np.array([house_size, price ,acre_lot])
print("price plus size plus acre_lot - 3 dimension array:",d3_array)
print("shape:",d3_array.shape)
print("ndim:",d3_array.ndim)

#Slicing array
D2house_sizepriceslice = D2house_sizeprice[0:5:1] 
print(D2house_sizepriceslice) 

#indexing array
D2house_sizepricesliceitemonly = D2house_sizeprice[0:3]
print(D2house_sizepricesliceitemonly)

#if you don't need index values
for elem in np.nditer(D2house_sizeprice):
    print(elem)

#if you need index
for index, elem in np.ndenumerate(D2house_sizeprice):
    print(index,elem)