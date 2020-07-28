#Factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter a number to caculate it's factorial: "))
print("Factorial is:",factorial(n))

#%%
#Max marks
def marks():
    if(student1>student2 and student1>student3 and student1>student4 and student1>student5):
        print("Student 1 has max marks:",student1)
    elif(student2>student1 and student2>student3 and student2>student4 and student2>student5):
        print("Student 2 has max marks:",student2)
    elif(student3>student1 and student3>student2 and student3>student4 and student3>student5):
        print("Student 3 has max marks:",student3)
    elif(student4>student1 and student4>student2 and student4>student3 and student4>student5):
        print("Student 4 has max marks:",student4)
    elif(student5>student1 and student5>student2 and student5>student3 and student5>student4):
        print("Student 5 has max marks:",student5)
    else:
        print("No one student has maximum marks")

student1 = int(input("Enter marks for student 1: "))
student2 = int(input("Enter marks for student 2: "))
student3 = int(input("Enter marks for student 3: "))
student4 = int(input("Enter marks for student 4: "))
student5 = int(input("Enter marks for student 5: "))
print(marks())