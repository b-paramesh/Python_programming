'''write a program to input any character and check wheher it is alphabet, digit or special character?'''
def checking(data):
    if (data>='a' and data<='z') or (data>='A' and data<='Z'):#isalpha()
        return "Alphabet"
    elif int(data)>=0 and int(data)<=9:#isdigit()
        return "Digit"
    else:#special character
        return "Special Character"
print(checking(input("Enter any character:")))