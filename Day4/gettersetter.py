class data:
    def setter(self,p):
        self.p=p
    def getter(self):
        return self.p
d=data()
d.setter(input("enter a value:"))
print(d.getter())