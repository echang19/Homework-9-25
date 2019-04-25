'''
Created on Apr 2, 2019

@author: Evan A. Chang
Cryptography part 1
'''
def caesar_cypher(fname, encrypt, shift):
        
    fname=input("please enter a text file you want to decode")
    encryption=open('fname.txt','r')
    newtext=encryption.read()
   
    alpha=[]
    import string
    for c in string.ascii_lowercase:
        alpha.append(c)
    
    code=[]
    x=0
    #new encryption

    for i in range(0, 26):
        code.append=alpha[(x+3)%26]
        x+=1
    t=0
    new=0
    newEncryption=''
    for line in encryption:
        if encryption[t] !=code[new%26]:
            new+=1
        elif encryption[t]==code[new]:
            newEncryption.append=code[new],sep=''
            t+=1
        elif encryption[t].isupper():
            code.upper()
        elif encryption[t].islower():
            code.lower()
    length=len(newEncryption)
    print(newEncryption)
    Test_ENC=open('newEncryption','w')
    for i in length:
        Test_ENC.write('newEncryption')
    Test_ENC.close()
    print(newEncryption)
            
            
            
        
        
caesar()   