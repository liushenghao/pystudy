class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def backTop(self):
        return self.items[len(self.items)-1]
    def sizeOf(self):
        return len(self.items)
    def pushIn(self,number):
        self.items.append(number)
    def pullOut(self):
        return self.items.pop()

def main():
    stack = Stack()
    print('empty or not?',stack.isEmpty())
    stack.pushIn(1)
    stack.pushIn(12)
    stack.pushIn(123)
    print('empty or not?',stack.isEmpty())
    print('length is:',stack.sizeOf())
    print('pull out :',stack.pullOut())
    print('now the top is',stack.backTop())
    print('pull out :',stack.pullOut())
    print('pull out :',stack.pullOut())
    print('empty or not?',stack.isEmpty())
    print('length is:',stack.sizeOf())

if __name__ == "__main__":
    main()

