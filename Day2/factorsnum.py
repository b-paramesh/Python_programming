def factors(n):
    for i in range(1,(n//2)+2):
        if n%i==0:
            print(i,end=" ")
factors(int(input("Enter value:")))