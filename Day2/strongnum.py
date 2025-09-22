def fact(p):
    fg=1
    for i in range(1,p+1):
        fg*=i
    return fg
def sumdigit(n):
    for i in range(1,n+1):
        num=i
        sum=0
        r=0
        while num>0:
            r=num%10
            sum=sum+fact(r)
            num=num//10
        if sum==i:
            print(i,end=" ")
sumdigit(int(input("Enter a number:")))