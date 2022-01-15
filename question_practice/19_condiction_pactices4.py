#Q. write a program to find whether a given username contains less than 10 characters or not.
username=input("Enter your name\n")
print(len(username))
if(len(username)<10):
    print("username contain less than 10 characters")
else:
    print("username contain greater than 10 characters")