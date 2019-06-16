class ListInstanceAttr:
    def __init__(self,a):
        self.a=a
        print('this is init A')

class B(ListInstanceAttr):
    def __init__(self,a):
        super(B,self).__init__(a)
        print('this is init B')

class C(ListInstanceAttr):
    def __init__(self,a):
        super(C,self).__init__(a)
        print('this is init C')

class D(B,C):
    def __init__(self,a):
        super(D,self).__init__(a)
        print('this is init D')

def main():
    d=D('d')
    print(d.a)
    for i in dir(D):
        print(i,':',getattr(d,str(i)))

if __name__ == "__main__":
    main()