'''
Created on Apr 2, 2019

@author: Evan A. Chang
Cryptography part 3
'''
def main():
    #ask me if i want to encrypt/decrypt
    fname=input("please enter a text file you want to encode/decode or crack")
    encrypt=input("Would you like to encrypt or decrypt or crack a file?")
    #ask me shift

    shift=int(input("how many spaces do you want to shift the alphabet to code"))
    caesar_cypher(fname, encrypt, shift)
    #all caesar_cypher with that info as arguments
    #store the result in variable
    #write it to new file
   
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
        
    
    
    #Crack
    elif encrypt.lower()=='crack':
        cracked_code=''
        x=0
        for line in encryption:
            cracked_code.append=alpha[(x+1)%26]
            
        print(cracked code[0-100])
        cracked=input("Is this code cracked?")
        if cracked.lower()=='yes':
            test_DEC=open('newDecryption','w')
            length=len(newDecryption)
            for i in length:
                test_DEC.write('newDecryption')
                test_DEC.close()
        print("the decrypted code has been written to test_DEC ")
        
        elif cracked.lower()== 'no':
            

        
        
       

  





main() 