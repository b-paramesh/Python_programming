def func(a,b):
    c=0
    for i in a:
        c+=1
    print("String 1:",c)
    print("comparing strings:",a==b)
    print("concatinate:",a+b)
func(input("string 1:"),input("string2:"))