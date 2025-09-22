def divisorsum(p):
    sum=0
    for i in range(1,(p//2)+1):
        if p%i==0:
            sum+=i
    return sum
def perfectnum(n):
    for i in range(1,n+1):
        if divisorsum(i)==i:
            print(i,end=" ")
perfectnum(int(input("Enter a value:")))