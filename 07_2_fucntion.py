#n!=1*2*3*4*5....
#n=4
#product=1
#for i in range(n):
 #   product=product+(i+1) 
#print(product)
def factorial(n):
    if n==0 or n==1 :
        return 1
    else:
        return n*factorial(n-1)
f=factorial(4)
print(f)