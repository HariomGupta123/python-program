try:
    a=int(input("Enter a number:"))
    c=1/a
    print(c)
except Exception as e:
    print(e)
except ValueError as e:
    print("Enter the valid value")
except ZeroDivisionError as e:
    print("Make sure u are not dividing by 0")
    
print("that's good things")