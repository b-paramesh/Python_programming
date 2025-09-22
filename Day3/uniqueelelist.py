def func(l1,n):
    l2=[]
    for i in range(n):
        if l1[i] not in l2:
            l2=l2+[l1[i]]
    print(l2)
n=int(input("Value:"))
l1=[]
for i in range(n):
    l1=l1+[int(input())]
func(l1,n)