def firstlast(n):
    l1=str(n)
    return f"{l1[0]} is first\n {l1[len(l1)-1]} is last"
print(firstlast(int(input("Enter n value:"))))