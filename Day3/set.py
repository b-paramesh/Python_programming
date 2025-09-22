'''Set Methodes'''
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a|b)

a={1,3,4,6,7,8}
b={4,5,6,73,3}
print(a.union(b))

a={1,2,3,4,5}
b={4,5,6,7,8}
print(a&b)

a={1,3,4,6,7,8}
b={4,5,6,73,3}
print(a.intersection(b))

a={1,2,3,4,5}
b={4,5,6,7,8}
print(a-b)

a={1,3,4,6,7,8}
b={4,5,6,73,3}
print(a.difference(b))

a={1,2,3,4,5}
b={4,5,6,7,8}
print(a^b)

a={1,3,4,6,7,8}
b={4,5,6,73,3}
print(a.symmetric_difference(b))

a={7,8,5,36424,56}
print(sorted(a))