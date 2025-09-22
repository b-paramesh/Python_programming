def func(sts):
    vowel=0
    cons=0
    for i in sts:
        if i.lower() in ('a','e','i','o','u'):
            vowel+=1
        elif i.isalpha():
            cons+=1
    print("Vowels:",vowel,"\nconsonents:",cons)
func(input("String:"))