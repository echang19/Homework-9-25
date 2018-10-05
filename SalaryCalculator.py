'''
Created on Oct 5, 2018

@author: Evan A Chang
'''
rate=float(input('Please inscribe your hourly rate'))
Hours=float(input('Please enter the average hours you work in a week'))

#Calculations
week=rate*Hours
month=week*4
year=month*12

print(format(week,'5.2f'))
print(format(month,'5.2f'))
print(format(year, '5.2f'))