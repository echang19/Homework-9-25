'''
Created on Apr 2, 2019

@author: Evan A. Chang
Cryptography
'''
def cypher.py():
    
    text=input("please enter a text file you want to decode")
    encryption=open(text,'r')
    code1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"A",'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    code2=[]
    x=0
    #new encryption
    crypt=int(input('How many spaces would would you care to shift your alphabet'))
    for i in range(0, 52):
        code2.append=code1[(x+crypt)%52]
        x+=1
    t=0
    for i in range text
    
    
    