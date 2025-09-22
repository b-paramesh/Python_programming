consumernum=int(input("consumer number:"))
consumername=input("consumer name:")
pmr=float(input("present month reading:"))
lmr=float(input("last month reading:"))
tu=pmr-lmr
cbill=tu*3.80
print("consumername:",consumername,"\nconsumernumber:",consumernum,"\npresent month reading:",pmr,
"\nlast month reading:",lmr,"\ntotal unit:",tu,"\nbill amount:",cbill)