def additem(l1,item):
    l1.append(item)
def removeitem(l1,item):
    if len(l1)==0:
        print("Empty")
        return
    l1.remove(item)
def searchitem(l1,item):
    if len(l1)==0:
        print("Empty")
        return
    for i in l1:
        if i==item:
            print("item found",item)
        return
    print("Not found")
def displayitem(l1):
    if len(l1)==0:
        print("Empty")
    for i in l1:
        print(i,end="\n")
def totalproductitem(l1):
    print("Count of products:",len(l1))
def sortcart(l1):
    print("Sorting")
    l1.sort()
    print("Sorted cart",l1)
def clearCart(l1):
    print("Clearing")
    l1.clear()
    print("Cart:",l1)


l1=[]
k=1
p=0
while k==1:
    print("Enter :\n1 add:\n2 remove:\n3 search:\n4 display:\n5 show total:")
    p=int(input())
    if p==1:
        o=int(input("Adding item:"))
        additem(l1,o)
    elif p==2:
        o=int(input("removing item:"))
    elif p==3:
        searchitem(l1,int(input("searchingitem")))
    elif p==4:
        print("displaying")
        displayitem(l1)
    elif p==5:
        print("number of products:")
        totalproductitem(l1)
    elif p==6:
        sortcart()
    elif p==7:
        clearCart()
    else:
        print("Invalid option")
        exit(1)
    print("k==1 for returning menu")
    k=int(input())