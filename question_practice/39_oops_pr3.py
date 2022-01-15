class train:
    def __init__(self,trainname,seat,fareinfo):
        self.trainname= trainname
        self.seat= seat
        self.fareinfo= fareinfo
    def gettrainname(self):
        print(f"the train {self.trainname}")

    def getseat(self):
        print(f"The number of seat available in train {self.trainname} is :{self.seat}")

    def getfareinfo(self):
        print(f"the fare of the train{self.trainname} is Rs:{self.fareinfo}")
    def bookseat(self):
        if (self.seat>0):
           print(f"seat are available {self.seat}")
           self.seat=self.seat-1
        else:
           print("sorry!this train is full kindly try takal")
    def cancelseat(self):
        

        


janakpurexpress = train("janakpurexpress",3,"500")
janakpurexpress.gettrainname()
janakpurexpress.getseat()
janakpurexpress.getfareinfo()
janakpurexpress.bookseat()

