def func(n):
    l2=[]
    for i in range(n):
        k=int(input())
        l2=l2+[k]
    m1=l2[0]
    m2=l2[0]
    for i in range(n):
        if m1<l2[i]:
            m1=l2[i]
    for i in range(n):
        if m2<l2[i] and l2[i]!=m1:
            m2=l2[i]
    print(m2)
n=int(input("Enter n:"))
func(n)