def div5and11(num):
    if num%5==0 and num%11==0:
        print("divisible by 5 and 11")
    else:
        print("not divisible by 5 and 11")
div5and11(int(input('Enter a value:')))