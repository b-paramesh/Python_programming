def func(n):
    l2=[]
    for i in range(n):
        k=int(input())
        l2=l2+[k]
    l1=[]
    for i in range(n):
        c=1
        for j in range(i+1,n):
            if l2[j]==l2[i] and l2[i] not in l1:
                c+=1
        if l2[i] not in l1:
            print(l2[i],"->",c)
        l1+=[l2[i]]
func(int(input("Enter value:")))