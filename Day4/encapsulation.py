class car:
    def __init__(self,s1,s2,s3):
        self.__s1=s1
        self._s2=s2
        self.s3=s3
    def display1(self):
        print(self.__s1)
    def display2(self):
        print(self._s2)
    def display3(self):
        print(self.s3)
c=car(1,2,3)
c.display1()
c.display2()
c.display3()