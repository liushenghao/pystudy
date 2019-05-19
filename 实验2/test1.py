str = input()
length = len(str)
up=low=num=other=0
for i in range(length):
    asc= ord(str[i])
    if asc>47 and asc<58:
        num+=1
    elif asc>64 and asc<91:
        up+=1
    elif asc>96 and asc<123:
        low+=1
    else:
        other+=1
tup = (up,low,num,other)
print(tup)
