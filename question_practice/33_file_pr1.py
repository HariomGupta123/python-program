#Q.write a program to read  a text from the given file sample.txt and find out the whether the contain the word "everyone".
f=open('adhura.txt','r')
a=f.read()
if "nature" in a:
    print("present")
else:
    print("not present")
f.close()