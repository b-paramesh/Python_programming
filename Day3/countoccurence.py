def occurences(st):
    p=""
    p1=[]
    p2=[]
    for i in range(len(st)):
        c=0
        for j in range(len(st)):
            if st[j]==st[i] and st[j] not in p1:
                p+=st[j]
                p1.append(st[i])
            if st[j]==st[i]:
                c+=1
        if st[i] not in p2:
            p2.append(st[i])
            p+=str(c)
    print(p)
occurences(input("string:"))