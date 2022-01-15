while(True):
    print("Press q to quite")
    a=input("Enter a number:")
    
    if a == 'q':
        break
    try:
       a=int(a)

       if a>5:
        print("The entered number is greater than 5")

    
    except Exception as r:
         print(r)
print("thanks you!,for u playing the game")

