'''
Created on May 17, 2019

@author: Evan A. Chang


'''

'''
Created on Apr 2, 2019

@author: Evan A. Chang
Cryptography part 4
'''
def main():
    #ask me if i want to encrypt/decrypt
    import random
    fname=input("please enter a text file you want to encode/decode or crack")
    encrypt=input("Would you like to encrypt or decrypt or crack a file?")
    al=input("would you like to use caesar or permutated alphabet (use c for caesar and p for permutation")
    

    #ask me shift
    if al.lower()=='c':
        shift=int(input("how many spaces do you want to shift the alphabet to code"))
        caesar_cipher(fname, encrypt, shift)
    #all caesar_cypher with that info as arguments
    #store the result in variable
    #write it to new file
    
    elif al.lower()=='p': 
        alpha=[]
        import string
        for c in string.ascii_lowercase:
            alpha.append(c)
    

    
    perm=[]
    for line in alpha:
        permutated=random.randint(1-27)
        perm.append(alpha[permutated])
    print("your new alphabet is",perm)
    perm_cipher(fname, encrypt, perm)
        
   
    if encrypt.lower()=="encrypt":
        
        test_ENC=open('newEncryption','w')
        length=len(newEncryption)
            for i in length:
                test_ENC.write('newEncryption')
                test_ENC.close()
            print("your code has been written to file test_ENC")
                
    elif encrypt.lower()=='decrypt':
        test_DEC=open('newDecryption','w')
        length=len(newDecryption)
        for i in length:
            test_DEC.write('newDecryption')
            test_DEC.close()
        print("the decrypted code has been written to test_DEC ")
    
    

def caesar_cipher(fname, encrypt, shift):
    
   
    
    
    
    if encrypt.lower()=="encrypt":
        
        encryption=open(fname.txt,'r')
        newtext=encryption.read()
   
        alpha=[]
        import string
        for c in string.ascii_lowercase:
            alpha.append(c)
    
            code=[]
            x=0
    #new encryption
        
        for i in range(0, 26):
            code.append=alpha[(x+shift)%26]
            x+=1
        t=0
        new=0
        newEncryption=''
        for line in encryption:
            if encryption[t] !=code[new%26]:
                new +=1
            elif encryption[t]==code[new]:
                newEncryption.append=code[new],sep=''
                t+=1
            elif encryption[t].isupper():
                code.upper()
            elif encryption[t].islower():
                code.lower()
                
            
    
    #Decryption
    elif encrypt.lower()=="decrypt":
        
        encryption=open(fname.txt,'r')
        newtext=encryption.read()
        
        alpha=[]
        import string
        for c in string.ascii_lowercase:
            alpha.append(c)
        code=[]
        x=0
    #new decryption
        shift=int(input("how many spaces do you want to shift the alphabet to code"))
        for i in range(0, 26):
            code.append=alpha[(x+shift)%26]
            x+=1
        t=0
        new=0
        newDecryption=''
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
        
    
    
    #Crack
    elif encrypt.lower()=='crack':
        cracked_code=''
        x=0
        for line in encryption:
            encryption[x]=alpha[x]
            cracked_code.append=encryption[x]
            x+=1
        print(cracked_code[0-100])
        cracked=input("Is this code cracked?")
        
        while cracked.lower()== 'no':
            for line in encryption:
            encryption[x]=alpha[x]
            cracked_code.append=encryption[x]
            x+=1
            print(cracked_code[0-100])
            cracked=input("Is this code cracked?") 

        if cracked.lower()=='yes':
            test_DEC=open('newDecryption','w')
            length=len(newDecryption)
            for i in length:
                test_DEC.write('newDecryption')
                test_DEC.close()
        print("the decrypted code has been written to test_DEC ")
        
def perm_cipher(fname, encrypt, perm):
    if encrypt.lower()=="encrypt":
        
        encryption=open(fname.txt,'r')
        newtext=encryption.read()
   
        alpha=[]
        import string
        for c in string.ascii_lowercase:
            alpha.append(c)
    
            code=[]
            x=0
    #new encryption
        
        for i in range(0, 26):
            code.append=alpha[(x+shift)%26]
            x+=1
        t=0
        new=0
        newEncryption=''
        for line in encryption:
            if encryption[t] !=code[new%26]:
                new +=1
            elif encryption[t]==code[new]:
                newEncryption.append=code[new],sep=''
                t+=1
            elif encryption[t].isupper():
                code.upper()
            elif encryption[t].islower():
                code.lower()
                
            
    
    #Decryption
    elif encrypt.lower()=="decrypt":
        
        encryption=open(fname.txt,'r')
        newtext=encryption.read()
        
        alpha=[]
        import string
        for c in string.ascii_lowercase:
            alpha.append(c)
        code=[]
        x=0
           
       

  


main() 