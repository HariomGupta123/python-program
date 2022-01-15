try:
    i=int(input("Entre a number:"))
    a=1/i
    print(a)
except Exception as e:
    print(e)
finally:
    print("we are done")
print("thanks u")
