def armstrong(n):
    for i in range(1,n+1):
        sum=0
        r=0
        n=i
        while n>0:
            r=n%10
            sum=sum+r*r*r
            n=n//10
        if sum==i:
            print(i,end=" ")
armstrong(int(input("Enter a number:")))