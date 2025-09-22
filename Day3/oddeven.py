def func(n):
    l1=[]
    l2=[]
    for i in range(n):
        k=int(input())
        if k%2==0:
            l1=l1+[k]
            continue
        l2=l2+[k]
    print(l1,"\n",l2)
func(int(input("Enter n:")))