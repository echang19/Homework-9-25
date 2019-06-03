def main():
    import random
    class Die:
        def __init__(self, v):
            self.__value=v
            
        def get_value(self):
            return self.__value
        
            
        def roll(self):
            self.__value= random.randint(1,6)
    class Yahtzee():   
        def __init__(self, Die): 
            
   
    
    
    d1=Die()    
    d2=Die()
    d3=Die()
    d4=Die()
    d5=Die()
    
    
    
