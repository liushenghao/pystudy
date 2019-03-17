x=3
y=x
#此时多个不同变量指向同一个值
print(id(x),id(y))
x+=3
print(id(x),id(y))
#python有自带的内存管理系统，无需担心内存。
