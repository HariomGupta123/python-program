#Q.write a program to find factorial of the which entered by user.
n=int(input("Enter a number"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
    print(f"the fatorial of {n} is {factorial}")