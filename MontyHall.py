'''
Created on Nov 16, 2018

@author: Evan A. Chang
'''
#random function
import random
car= random.randint(1,3)
goat= not car

guess=int(input("please pick a door you think has the Car (1, 2 , or 3)"))


#if their guesss is one

if guess==1 and car==3:
    print("there was a goat behind door 2")
    g2=input("Would you like to switch doors?")
    if g2.lower()=='yes':
        print("Congratulations you got the car!!")
    else:
        print("The prize was behind door 3 sorry")
elif guess==1==car:
    print("there was a goat behind door 2")
    g2=input("Would you like to switch doors?")
    if g2.lower()=='no':
        print("Congratulations you got the car!!")
    else:
        print("The prize was behind door 1 sorry")
elif guess==1 and car==2:
    print("there was a goat behind door 3")
    g2=input("Would you like to switch doors?")
    if g2.lower()=='yes':
        print("Congratulations you got the car!!")
    else:
        print("The prize was behind door 2 sorry")


#if they guessed door 2
elif guess==2 and car==1:
    print("there was a goat behind door 3")
    g2=input("Would you like to switch doors?")
    if g2.lower()=='yes':
        print("Congratulations you got the car!!")
    else:
        print("The prize was behind door 1 sorry")
elif guess==2 and car==3:
    print("there was a goat behind door 1")
    g2=input("Would you like to switch doors?")
    if g2.lower()=='yes':
        print("Congratulations you got the car!!")
    else:
        print("The prize was behind door 3 sorry")
elif guess==2==car:
    print("there was a goat behind door 1")
    g2=input("Would you like to switch doors?")
    if g2.lower()=='no':
        print("Congratulations you got the car!!")
    else:
        print("The prize was behind door 2 sorry")

#if they guessed door 3


elif guess==3 and car==1:
    print("there was a goat behind door 2")
    g2=input("Would you like to switch doors?")
    if g2.lower()=='yes':
        print("Congratulations you got the car!!")
    else:
        print("The prize was behind door 1 sorry")
elif guess==3 and car==2:
    print("there was a goat behind door ")
    g2=input("Would you like to switch doors?")
    if g2.lower()=='yes':
        print("Congratulations you got the car!!")
    else:
        print("The prize was behind door 2 sorry")
elif guess==3==car:
    print("there was a goat behind door 1")
    g2=input("Would you like to switch doors?")
    if g2.lower()=='no':
        print("Congratulations you got the car!!")
    else:
        print("The prize was behind door 3 sorry")
