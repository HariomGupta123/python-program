with open('sample.txt','r') as f:
    a=f.read()
    a=a.replace("khan","********")
with open('sample.txt','w') as f:
    f.write(a)