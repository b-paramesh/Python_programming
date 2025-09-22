def occurence(st,ch):
    i=0
    pos=[]
    while i<len(st):
        if st[i]==ch:
            pos.append(i)
        i+=1
    return pos
st=input("String:")
p=input("character:")
print(occurence(st,p))
