def f(x):
    if(x<0):
        y=0
    elif(x<5 and x>=0):
        y=x
    elif(x<10 and x>=5):
        y=3*x-5
    elif(x<20 and x>=10):
        y=0.5*x-2
    else:
        y=0
    return y

x=int(input())
print(f(x))
