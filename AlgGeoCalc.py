'''
Created on Oct 15, 2018

@author: Evan Chang
'''
name=input('Please input your name')
print('Hello,', name, 'welcome to the Algebra and Geometry Calculator')
input('Press Enter to Continue')
print('Area of a Triangle:')
B=float(input("please enter the base of the triangle"))
H=float(input("please input the height of the triangle"))
AT=0.5*B*H
print('The Area of the Triangle is', format(AT,'3,.2f', 'cm^2'))
input('Press Enter to Continue')
print("Volume of A Cube:")
B1=float(input('Please enter the base of the cube'))
H2=float(input('Please enter the height of the cube'))
W=float(input('Please enter the width of the cube'))
CV=B1*H2*W
print(' The volume of the cube is', format(CV,'3,.2f', 'cm^3'))
print('Goodbye,', name, 'thank you for using this calculator')