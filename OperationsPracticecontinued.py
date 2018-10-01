'''
Created on Sep 27, 2018

@author: echang19
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
print('\n\n')

input('Press enter to find the slope  of a line')

x1=int(input('please enter x1'))
y1=int(input('please enter y1'))
x2=int(input('please enter x2'))
y2=int(input('please enter y2'))
slope=(y2-y1)/(x2-x1)

print('the slope of this line is', slope)
#calculation

print('\n')
# Price of an item
input('Press enter to find the total price of a shirt')
Shirt=float(input("Price of shirt" ))
SaleTax=(Shirt*0.06)
print('salestax:', SaleTax)
PRice=(Shirt*1.06)
print("\n\n")
print('the price of the shirt in total is', PRice)