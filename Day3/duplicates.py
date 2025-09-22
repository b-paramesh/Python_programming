def func(l1,n):
    l2=[]
    co=0
    for i in range(n):
        c=0
        for j in range(i+1,n):
            if l1[j]==l1[i]:
                co+=1
                l2+=[l1[i]]
                break
    print
n=int(input("Enter value:"))
l1=[]
for i in range(n):
    l1=l1+[int(input())]
func(l1,n)