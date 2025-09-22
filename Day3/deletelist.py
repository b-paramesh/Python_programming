def func(n):
    l1=[]
    for i in range(n):
        l1=l1+[int(input())]
    p=int(input("Enter pos:"))
    l2=[]
    c=0
    for i in range(n):
        if i==p:
            l1[i]=False
            continue
        c+=1
    for i in range(c+1):
        if l1[i]:
            l2=l2+[l1[i]]
    print(l2)
func(int(input("Enter num:")))