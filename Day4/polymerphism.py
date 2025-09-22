class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("name:",self.name,"salary:",self.salary)
class Manager(Employee):
    def __init__(self,name,salary,department):
        self.department=department
        super().__init__(name,salary)
    def display(self):
        print("name:",self.name,"salary:",self.salary,"department:",self.department)
name=input("name:")
salary=int(input("salary:"))
depa=int(input("department:"))
em=Employee(name,salary)
ma=Manager(name,salary,depa)
em.display()
ma.display()