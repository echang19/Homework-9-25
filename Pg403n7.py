'''
Created on Feb 28, 2019

@author: Evan A. Chang
Driver's License
'''
def main():
    cor=0
    correct=["A", 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    
    student=open('Test.txt', 'r')
    #in a loop student.append()
    
    x=0
    while len(correct)== len(student) and x<=20:
        if correct[x]==student[x]:
            x +=1
            cor +=1
        else:
            x +=1
               
            
             
    if cor < 15:
        print("You failed the test")
    else:
        print("Congratulations you passed with a score of", cor, "/20")    


