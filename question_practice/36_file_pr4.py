words=["love","blind","sing","hero"]
with open('sample.txt','r') as f:
    a=f.read()
for word in words:
    a=a.replace(word,"********")
with open('sample.txt','w') as f:
    f.write(a)