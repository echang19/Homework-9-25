'''
Created on Apr 2, 2019

@author: Evan A. Chang
Cryptography part 1
'''
def main():
    #ask me if i want to encrypt/decrypt
    fname=input("please enter a text file you want to encode/decode")
    encrypt=input("Would you like to encrypt or decrypt a file?")
    #ask me shift

    shift=int(input("how many spaces do you want to shift the alphabet to code"))
    
    #all caesar_cypher with that info as arguments
    #store the result in variable
    #write it to new file
    

def caesar_cypher(fname, encrypt, shift):
    
    
    if encrypt.lower()=="encrypt":
        
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
                length=len(newEncryption)
            
    
    #Decryption
    elif encrypt.lower()=="decrypt":
        
        encryption=open('fname.txt','r')
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
        length=len(newDecryption)
       

caesar_cypher(fname, encrypt, shift)  
    if encrypt.lower()=="encrypt":
        test_ENC=open('newEncryption','w')
            for i in length:
                test_ENC.write('newEncryption')
                test_ENC.close()
            print("your code has been written to file test_ENC")
                
    elif encrypt.lower()=='decrypt':
        
        test_DEC=open('newDecryption','w')
        for i in length:
            test_DEC.write('newDecryption')
            test_DEC.close()
        print("the decrypted code has been written to test_DEC ")
    




main() 