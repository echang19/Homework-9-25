'''
Created on Apr 2, 2019

@author: Evan A. Chang
Cryptography part 1
'''
def main():    
    text=input("please enter a text file you want to decode")
    encryption=open('text','r')
    newtext=encryption.read()
    newtext.close()
    alpha=[]
    import string
    for c in string.ascii_lowercase:
        alpha.append(c)
    
    code=[]
    x=0
    #new encryption
    crypt=int(input('How many spaces would would you care to shift your alphabet'))
    for i in range(0, 26):
        code.append=alpha[(x+crypt)%26]
        x+=1
    t=0
    new=0
    newEncryption=''
    for line in encryption:
        if encryption[t] !=alpha[new%26]:
            new+=1
        elif encryption[t]==alpha[new]:
            newEncryption.append=code[new],sep=''
            t+=1
        elif encryption[t].isupper():
            alpha.upper()
        elif encryption[t].islower():
            alpha.lower()
    Test_ENC=open('newEncryption','w')
    print(newEncryption)
            
            
            
        
        
main()   