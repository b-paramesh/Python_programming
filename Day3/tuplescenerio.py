def menu(l1):
    while True:
        def adding():
            name=input("name:")
            rollno=int(input("rollno:"))
            marks=int(input("marks:"))
            l1.append((name,rollno,marks))
            print("k==1 for exit")
        def returning():
            return
        def highest():
            name=""
            ma=l1[0][2]
            for i in range(len(l1)):
                if ma<l1[i][2]:
                    name=l1[i][0]
            print(name)
        def printscore75():
            for i in range(len(l1)):
                if l1[i][2]>75:
                    print(l1[i][0])
        print("1 adding:\n2 highest mark:\n3 above 75: \n 4 exit :")
        k=int(input())
        if k==1:
            adding()
        elif k==2:
            highest()
        elif k==3:
            printscore75()
        else:
            returning()
        

l1=[]
menu(l1)