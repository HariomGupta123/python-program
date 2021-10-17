# Q.write a program to fill in a letter templet to given below with name and date.
letter='''Dear, <|NAME|>

you are selected,


<|DATE|>
'''
name=input("enter your name\n")
date=input("enter date\n")
letter=letter.replace("<|NAME|>",name)
lette=letter.replace("<|DATE|>",date)
print(letter)