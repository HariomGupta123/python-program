#Q.write a program to multiplication of number input by user using for loop.
num=int(input("enter a number"))
i=0
'''#for i in range(1,11):
    print(f"{num}X{i}={num*i}")
    #print(str(num) + "*" +str(i) + "=" + str(i*num) )
    #print(str(i*num))'''
while i<11:
    #print(str(num) + "*" +str(i) + "=" + str(i*num) )
    #print(f"{num}X{i}={num*i}")
    print(str(i*num))
    i=i+1

else:
    print("done")
