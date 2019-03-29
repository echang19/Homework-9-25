'''
Created on Mar 12, 2019

@author: Evan A. Chang
Grade Report
'''
def main():
    studentList={'Cooper':['81','86', '90', '97'],'Jennie':['98', '79','99', '87', '82'], 'Julia':['87', '80','75', '10', '78']}
    student=''
    read=input("Would you like to access a student's grades?")
    read.lower()
    if read== "no":
        student= input("Please enter the name of a student")
        student.str
        grades=''
        while grades.lower !='done':
            grades=input('please enter the students grades when done type "done" ')
            grades.str
            studentList[student]=grades
    elif read=="yes":
        name=input("Please enter the name of the student you want to see")
        print(studentList[name])
        again=input("would you like to see another's students grades?")
        while again.lower()=='yes':
            name=input("Please enter the name of the student you want to see")
            print(studentList[name])
    
