def isprime(n):
    if n==1:
        return "Not a prime"
    for i in range(2,n//2+1):
        if n%i==0:
            return "Not a prime"
    return "Prime"
print(isprime(int(input("Enter the value:"))))