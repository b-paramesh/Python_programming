class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print("name:",self.name,"\nrollno:",self.rollno,"\nmarks:",self.marks)
name=input("name:")
rollno=int(input("Roll no:"))
marks=int(input("marks:"))
student =Student(name,rollno,marks)
student.display()


name=input("name:")
rollno=int(input("Roll no:"))
marks=int(input("marks:"))
student1 =Student(name,rollno,marks)
student1.display()