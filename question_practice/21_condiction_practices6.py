# Q.write a program calculate the grade of a student from his marks thr following scheme ["90-100=ex",80-90=A,70-80=B,60-70=c,50-60=D]
marks=int(input("Enter the marks of a student\n")) 

if(marks>90 and marks<100):
    print("exe")
if(marks>80 and marks<90):
        print("A")
if(marks>70 and marks<80):
        print("B")
if(marks>60 and marks<70):
        print("C")
if(marks>50 and marks<60):
        print("D")
if(marks>50 and marks<100):
    print("u passed in exam")
else:
    print("u failed in exam")


