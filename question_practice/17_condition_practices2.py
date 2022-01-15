sub1=int(input("Enter fisrt subject marks\n"))
sub2=int(input("Enter second subject marks\n"))
sub3=int(input("Enter third subject marks\n"))
marks={sub1,sub2,sub3}
print(marks)

if(sub1<33 or sub2<33 or sub3<33):

    print("you are failed the exam becouse u obtained less than 33 marks in some subject")
elif((sub1+sub2+sub3)/3<40):
    print("you are failed in the exam becouse u obtained less than 40% in total subjects")
else:
    print("congratulations! u fassed the exam")
