def percent(marks):
    return ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
marks1=[89,87,99,96]
percentage1=percent(marks1)
marks2=[99,69,79,80]
percentage2=percent(marks2)
print(percentage1,percentage2)
#Q.write a progra to greet a user "good morning" using function.
def greet(name):
    print("Good morning," + name)
def mysum(num1,num2):
    return num1+num2
greet("hari")
s=mysum(45,34)
print(s)