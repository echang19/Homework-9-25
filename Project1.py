'''
Created on Sep 27, 2018

@author: Evan A Chang

Project 1 Input and Operations
Mr. Ellis Pd.5
'''
Name=input("Please type your name:" )
print('\n\n')
Phone=input('Please insert your phone number')
print('\n\n')
Item=input('Please insert the product you would like to purchase')
print('\n')
Price=float(input('Price of item is $'))
Q=float(input('Quantity of item:'))
print('\n\n\n')
print(Name)
print('\n')
print(Phone)
print('\n')
print('Purchase Information')
print('\n')
print(Item, 'Qty:', Q, 'Price: $', Price)

#Price and tax


Subtotal=Price*Q
tax=Subtotal*0.06
Total=Subtotal+tax
print()
print('Subtotal: $', Subtotal, 'Tax: $', tax, 'Total $', Total)