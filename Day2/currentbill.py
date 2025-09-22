def currentBill(units):
    if units>300:
      bill=(units-300)*7.50+100*6.30+100*5.10+50*4.20+50*3.80
    elif units<=300 and units>200:
       bill=(units-200)*6.30+100*5.10+50*4.20+50*3.80
    elif units>100 and units<=200:
      bill =(units-100)*5.10+50*4.20+50*3.80
    elif units>50 and units<=100:
       bill=(units-50)*4.20+50*3.80
    else:
       bill=units*3.80
    return bill
pmb=int(input("prsesent month bill:"))
lmb=int(input("last month bill:"))
print(currentBill(pmb-lmb))