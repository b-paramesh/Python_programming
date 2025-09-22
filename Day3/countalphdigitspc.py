n=input("String:")
alpha=0
digit=0
special=0
for i in n:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        digit+=1
    else:
        special+=1
print("alphabets:",alpha,"\ndigits:",digit,"\nspecial characters:",special)