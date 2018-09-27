'''
Created on Sep 26, 2018

@author: Evan Chang
'''


print('welcome to the test score calculator.')
print("\n\n\n\n")

# input the test scores
test1=float(input("Please enter the first test score: "))
test2=float(input("Please enter the second test score: "))
test3=float(input("Please enter the third test score: "))

# calculate the average
average=(test1+test2+test3)/3

#display the output
print("Average Test Score", average)

# find slope
point1x=float(5.0)
point1y=float(2.0)
point2x=float(10.0)
point2y=float(4.0)
slope=(point2y-point1y)/(point2x-point1x)

#calculation
print('the slope of this line is', slope)

# Price of an item
Shirt=float(input("Price of shirt" ))
SaleTax=(Shirt*0.06)
print('salestax:', SaleTax)
PRice=(Shirt*1.06)
print('the price of the shirt in total is', PRice)
