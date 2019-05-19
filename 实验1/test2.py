import random
x=[random.randint(0,1000) for i in range(20)]
d1=x[1:10]
d2=x[11:20]
d1.sort()
d2.sort()
d2.reverse()
print(d1+d2)