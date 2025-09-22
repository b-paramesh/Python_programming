n1=int(input("n1:"))
n2=int(input("n2:"))
try:
    div=n1%n2
    print("dividing:",div)
except ZeroDivisionError:
    print("Division by zero is not allowed.")