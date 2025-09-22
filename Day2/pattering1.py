def patterning(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()
print(patterning(int(input("Enter a value:"))))