sum =0
n = 0
a = int(input())
while a != 0:
    sum = a +sum
    n = n+1
    a =int(input())
result = float(sum/n)
print("The averenge of numbers is {:.2f}".format(result))
