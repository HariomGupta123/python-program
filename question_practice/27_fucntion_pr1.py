#Q.write a program to check the three number which is greater one.
def greater(num1,num2,num3):
    if (num1>num2):
        return num1
        if (num1>num3):
            return num1 
        else:
            return num3
    if (num2>num3):
        return num2    
    else:
        return num3 
g=greater(98,89,45)
print(g)    
