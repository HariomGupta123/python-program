#f=open("sample.txt",'r')
f=open("sample.txt")#by default the mode is "r"
data=f.read(5)#read 5 character from the file
print(data)
f.close()