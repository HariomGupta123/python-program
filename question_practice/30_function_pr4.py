#Q. write a recursive function to calculate the n natural number by using function.
#sum(n)=sum(n-1)+n
def sum(n):
    if n==0 :
        return 0
    else:
        return sum(n-1)+n
s=sum(20)
print(s)
