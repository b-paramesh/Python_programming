def firstlastsum(n):
    last=n%10
    sum=0
    while n>0:
        r=n%10
        sum=sum*10+r
        n=n//10
    return f"sum: {sum%10+last}"

print(firstlastsum(int(input("Enter value:"))))