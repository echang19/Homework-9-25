'''
Created on May 17, 2019

@author: Evan A. Chang
Yahtzee Part_1
'''
def main():
    import random
    class Die:
        def __init__(self, v=0):
            self.__value=v
            
        def get_value(self):
            return self.__value
        
            
        def roll(self):
            self.__value= random.randint(1,6)
        
    d1=Die(self,__value)    
    d2=Die(self,__value)
    d3=Die(self,__value)
    d4=Die(self,__value)
    d5=Die(self,__value)
    
    
    
