# Q.what is the length of the following set "s" 
s=set() #this is empty empty set
print(type(s))
#adding values in the empty set
s.add(3)
s.add(7)
s.add(8)
s.add(6)
s.add(1)
s.add(20)# s.add(20) and s.add(20.0) count once
s.add(20.0)
s.add("20")
print(s)
print(len(s))

