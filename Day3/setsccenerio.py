def fucn(s1,s2,s3):
    print("set1:",s1,"\nset2:",s2,"\nset3:",s3)
    print("total unique:",s1 | s2 |s3)
    print("three days:",s1 & s2 & s3)
    print("exactly one days:",s1 ^ s2 ^ s3)
    print("pair1:",s1&s2,"\npair2:",s2&s3,"\npair3:",s1&s3)
    print(sorted([[s1,s2,s3],[s1|s2|s3],[s1&s2&s3],[s1^s2^s3],[s1&s2,s2&s3,s1&s3]]))

s1,s2,s3=set(),set(),set()
n=int(input())
for i in range(n):
    s1.add(input("day1:").lower())
for j in range(n):
    s2.add(input("day2:").lower())
for k in range(n):
    s3.add(input("day3:").lower())
fucn(s1,s2,s3)