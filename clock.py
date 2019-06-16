import time
class Clock(object):
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
    def run(self):
        self.second+=1
        if self.second == 60:
            self.second =0
            self.minute+=1
            if self.minute == 60:
                self.minute = 0
                self.hour+=1
                if self.hour ==24:
                    self.hour=0
    def show(self):
        return ('%02d:%02d:%02d'%(self.hour,self.minute,self.second))

def main():
    clock1= Clock(22,00,50)
    
    while True:
        print(clock1.show())
        time.sleep(1)
        clock1.run()

if __name__ == "__main__":
    main()

