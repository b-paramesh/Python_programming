def days(day):
    year=day//365
    month=(day%365)//30
    print("year:",year,"\nmonth:",month)
days(int(input("days:")))