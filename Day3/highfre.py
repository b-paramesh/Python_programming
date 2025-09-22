def func(st):
    mx=st.count(st[0])
    o=st[0]
    for i in st:
        if mx<st.count(i):
            max=st.count(st[0])
            o=i
    print(o)
func(input("String:"))