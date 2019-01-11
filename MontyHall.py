'''
Created on Nov 16, 2018
@author: Evan A. Chang

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
'''


#Part 3 Simulation
print("Welcome to the Monty Hall simulator when asked how many rounds you would like to play please pick a number between 10 and 10000")
rnd=int(input("How many rounds should the game be simulated?"))



#Checking rounds
while rnd<10 or rnd>10000:
    rnd=int(input("that was an incorrect number try it again"))

import random
w=0
for rnd in range(0,rnd+1,):
    door=random.randint(1,4)
    car=random.randint(1,4)
    
    #if door is one
    if door==1 and car==1:
        switch=input("Do you want to switch or stay (say switch or stay)")
        while switch.lower()!="switch" and switch.lower() !="stay":
            switch=input('please enter "switch" or "stay"')
        if switch.lower()=="switch":
            print("sorry you lose")
        elif switch.lower()=="stay":
            print("you won")
            w+=1
    elif  door==1 and car==2:
        switch=input("Do you want to switch or stay (say switch or stay)")
        while switch.lower()!="switch" and switch.lower() !="stay":
            switch=input('Please enter "switch" or "stay"')
        if switch.lower()=="switch":
            print("you win")
            w+=1
        elif switch.lower()=="stay":
            print("you lost")
    elif  door==1 and car==3:
        switch=input("Do you want to switch or stay (say switch or stay)")
        while switch.lower()!="switch" and switch.lower() !="stay":
            switch=input('please enter "switch" or "stay"')
        if switch.lower()=="switch":
            print("you win")
            w+=1
        elif switch.lower()=="stay":
            print("you lost")      
               
            
            
    #Door 2    
    elif  door==2 and car==2:
        switch=input("Do you want to switch or stay (say switch or stay)")
        while switch.lower()!="switch" and switch.lower() !="stay":
            switch=input('please enter "switch" or "stay"')
        if switch.lower()=="switch":
            print("sorry you lose")
        elif switch.lower()=="stay":
            print("you won")
            w+=1
    elif  door==2 and car==1:
        switch=input("Do you want to switch or stay (say switch or stay)")
        while switch!="switch" and switch !="stay":
            switch=input('please enter "switch" or "stay"')
        if switch.lower()=="switch":
            print("you win")
            w+=1
        elif switch.lower()=="stay":
            print("you lost")         
    elif  door==2 and car==3:
        switch=input("Do you want to switch or stay (say switch or stay)")
        while switch.lower()!="switch" and switch.lower() !="stay":
            switch=input('please enter "switch" or "stay"')
        if switch.lower()=="switch":
            print("you win")
            w+=1
        elif switch.lower()=="stay":
            print("you lost")        
            

    
    
    
    
    #Door 3
    elif  door==3 and car==3:
        switch=input("Do you want to switch or stay (say switch or stay)")
        while switch.lower()!="switch" and switch.lower()!="stay":
            switch=input('please enter "switch" or "stay"')
        if switch.lower()=="switch":
            print("sorry you lose")
        elif switch.lower()=="stay":
            print("you won")
            w+=1
    elif  door==3 and car==1:
        switch=input("Do you want to switch or stay (say switch or stay)")
        while switch.lower()!="switch" and switch.lower() !="stay":
            switch=input('please enter "switch" or "stay"')
        if switch.lower()=="switch":
            print("you win")
            w+=1
        elif switch.lower()=="stay":
            print("you lost")     
    elif  door==3 and car==2:
        switch=input("Do you want to switch or stay (say switch or stay)")
        while switch.lower()!="switch" and switch.lower() !="stay":
            switch=input('please enter "switch" or "stay"')
        if switch.lower()=="switch":
            print("you win")
            w+=1
        elif switch.lower()=="stay":
            print("you lost")


per=w/rnd*100            
print("you win ", w, '/', rnd)
