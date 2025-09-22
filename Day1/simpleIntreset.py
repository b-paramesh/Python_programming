'''write a program to enter Principle Amount,Rate of Interest and Time to find Simple Interest and total Amount'''
pricipleAmount=int(input("enter the principle amount:"))
rateofIntreset=float(input("enter the rate of interest:"))
time=int(input("enter the time in mounths:"))
simpleinterest=(pricipleAmount*rateofIntreset*time)/100
totalAmount=pricipleAmount+simpleinterest
print("simple Intreset is",simpleinterest)
print("total Amount is",totalAmount)