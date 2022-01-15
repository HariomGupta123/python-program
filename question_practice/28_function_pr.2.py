#Q.write a program to conver celcius into fahrenhiet by using function.
def farh(cel):
    farh=(cel*(9/5))+32
    return farh
f=farh(4)
print("The tempareture is in ferh" + str(f))