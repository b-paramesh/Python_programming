def primerange(n):
    c=0
    for i in range(2,n):
        f=True
        for j in range(2,(i)//2+1):
            if i%j==0:
                f=False
                break
        if f:
            print(i,end=" ")
            c+=1
    print("\n",c)
primerange(int(input("Enter value:")))
