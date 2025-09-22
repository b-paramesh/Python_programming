def adding(d,k,v):
    d[k]=v
def removing(d,k):
    if k not in d:
        print("Not Found")
        return
    del d[k]
def search(d,j):
    for i in d.keys():
        if i==j:
            return f"found {d[i]}"
    return "Not Found"
def update(d,k,l1):
    if l1 not in d:
        print("Not Found")
        return
    d[k]=l1
def display(d):
    for i,j in d.items():
        print("key:",i,"value:",j)
def count(d):
    print(len(d))
def checking(d,p):
    if p in d:
        return "Exist"
    return "Not Exist"
d={}
while True:
    print("enter \n 1 adding:\n2 removing: \n3 searching:\n4 updateing:\n 5 displaying:\n6 counting \n7 checking:")
    k=int(input())
    if k==1:
        adding(d,int(input("enter id:")),input("title:"))
    elif k==2:
        removing(d,int(input("book id:")))
    elif k==3:
        print(search(d,int(input("searching id:"))))
    elif k==4:
        update(d,int(input("id change title"),input("new title")))
    elif k==5:
        display(d)
    elif k==6:
        count()
    elif k==7:
        print(checking(d,input("booking title searching:")))
    else:
        print("Invalid")
        break