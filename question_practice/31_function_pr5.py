#Q.write a python function to print firdt n lines of the following pattern
def parn(n):
 for i in range(n):
    print("*"*(n-i))
    #print("-"*(n-i),"+"*(n-i),"*"*(n-i),"0"*(n-i))
parn(3)