import random


def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='w':
       if you=='s':
        return True
       elif you=='g':
        return False
    elif comp=='s':
        if you=='w':
           return False
        elif you=='g':
            return True
    elif comp=='g':
        if you=='w':
            return True
        elif you=='s':
            return False


print("comp turn: water(w) snake(s) or gun(g)?")
randNo=random.randint(1,3)
print(randNo)
if randNo==1:
    comp='w'
elif randNo==2:
    comp='s'
elif randNo=='3':
    comp='g'
you=input("your turn: water(w) snake(s) or gun(g)?\n")
a= gameWin(comp,you)

print(f"comp choose {comp}")
print(f"you choose {you}")
if a==None:
    print("the game is a tied")
elif a:
    print("you win!")
else:
    print("you lose!")







