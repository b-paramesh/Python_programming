def isalpha(num):
    if (ord(num>=65 and ord(num)<=90) or (ord(num)>=97 and ord(num)<=122)):
        print("alphabet")
    else:
        print("not an alphabet")
# def isalpha1(num1):
#     if (num1>='a'and num1<='z') or (num1>='A' and num1<='Z'):
#         print("alphabet")
#     else:
#         print("not an alphabet")
n=input("enter char:")
isalpha(n)