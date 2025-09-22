from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class Circle(shape):
    def __init__(self,radius):
        self.radius=radius
        self.pi=3.14
    def area(self):
        return self.pi*self.radius*self.radius
r=Rectangle(int(input("length:")),int(input("breadth:")))
print(r.area())
c=Circle(int(input("radius:")))
print(c.area())