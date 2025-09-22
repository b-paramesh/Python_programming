def grading(mark):
    if mark<40:
        return "Fail"
    else:
        if mark>80:
            return "Distinction"
        elif mark<=80 and mark>=71:
            return "A"
        elif mark>=51 and mark<=70:
            return "B"
        else:
            return "C"
print(grading(int(input("Enter the marks:"))))