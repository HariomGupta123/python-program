#Q.write a program to create class for storing information of few programmer.
class Programmer:
    langauges="java"
    def __init__(self,name,age,codinglangauges):
        self.name=name
        self.age=age
        self.codinglangauges=codinglangauges
    def getdetial(self):
        print(f"programmer name:{self.name}")
        print(f"programmer age:{self.age}")
        print(f"programmer codinglaungaus:{self.codinglangauges}")
        
hari=Programmer("hari",23,"python")
hari.getdetial()

