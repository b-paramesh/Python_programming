def func(a):
    l2=[]
    for i in range(a):
        k=int(input())
        if k<0:
            l2=l2+[k]
    print(l2)
n=int(input("Enter n:"))
func(n)