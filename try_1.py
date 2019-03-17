amount=float(input())
inrate=float(input())
period=int(input())
value=0
year=0
while year <= period:
    value = amount +(inrate*amount)
    print("year{} RS. {:.2f}".format(year,value))
    amount = value
    year = year + 1