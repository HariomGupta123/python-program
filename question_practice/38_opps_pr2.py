#write a python program to calculate square,squareroot,cube,cuberoot of a number.
class calculate:
    def __init__(self,number) :
        self.number=number

        
    def getsquare(self):
        print(f"square of a number is:{self.number**2}")


    def getsquareroot(self):
        print(f"squareroot of a number {self.number} is:{self.number*0.5}")

    def getcube(self):
        print(f"cube of a number {self.number} is:{self.number**3}")
    def getcuberoot(self):
        print(f"cuberoot of a number {self.number}is:{self.number**0.33}")


a=calculate(9)
a.getsquare()
a.getsquareroot()
a.getcube()
a.getcuberoot()
        
    