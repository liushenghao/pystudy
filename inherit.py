import random
class Fish(object):
    def __init__(self):
        self.x=random.randint(0,10)
        self.y = random.randint(0,10)
    def move(self):
        self.x -=1
        self.y-=1
        print(" palce:%d,%d" % self.x,self.y)
class GoldFish(Fish):
    pass
class Crap(Fish):
    pass
class Salmo(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry =True
    def eat(self):
        if self.hungry:
            print('eat')
            self.hungry=False
        else:print('not hungry')