# Q.a spam comment is defined as a text containing following keywords("love","feeling","behavour","respect")
a=input("Enter the text\n")
if("love" in a):
    a=True
elif("respect" in a):
    a=True
elif("feelings" in a):
    a=True
elif("behevuor" in a):
    a=True
else:
    a=False
if(a):
    print("this is in a")
else:
    print("this is not in a")
    