#Q.write a program to check number is primary number or not.
num=int(input("Enter a number:\n"))
prime=True
for i in range(2,num):
    if (num%i==0):
        prime=False
        break
if prime:
    print("the number is prime number")
else:
    print("the number is not prime number")