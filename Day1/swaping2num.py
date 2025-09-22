'''write a python progrsm to swap of two numbrs'''
a=int(input("enter the a value:"))
b=int(input("enter the b value:"))
#swaping two variables using third variable
t=a
a=b
b=t
#swapping two variables without using third variable
a,b=b,a

a=a+b
b=a-b
a=a-b

a=a^b
b=a^b
a=a^b
print("after swaping a value is",a)
print("after swaping b value is",b)