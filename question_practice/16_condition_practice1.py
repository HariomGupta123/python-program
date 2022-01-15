#Q.find a greater number input by user among 4 numbers.
n1=int(input("enter a number1:\n"))
n2=int(input("enter a number2:\n"))
n3=int(input("enter a number3:\n"))
n4=int(input("enter a number4:\n"))
num={n1,n2,n3,n4}
print(num)
if(n1>n4):
    f1=n1
else:
    f1=n4
if(n2>n3):
    f2=n2
else:
    f2=n3
if(f1>f2):
    print(str(f1) + "f1 is greater")
else:
    print(str(f2) + "f2 is greater")