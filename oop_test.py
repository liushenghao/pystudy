class Ball(object):
    def __init__(self, name):
        self.name=name
    def kick(self):
        print("who kicks me? I am %s" %self.name)

a= Ball('A')
a.kick()
c= Ball('李佳佳')
c.kick()