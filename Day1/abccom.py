def com(a,b,c):
    if a>=b:
        if a>=c:
            print("a is greater")
        else:
            print("c is greater")
    else:
        if b>=c:
            print("b is greater")
        else:

            print("c is greater")
com(int(input("a:")),int(input("b:")),int(input("c:")))