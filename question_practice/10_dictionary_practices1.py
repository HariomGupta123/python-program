# Q.write a program to create dictionary of hindi words with value as theirs english traslations.provide user with an option to look its up.
MyDict={"ghar":"house",
"punkha":"fan",
"kapda":"cloth"}
print("options are",MyDict.keys())
Myword=input("enter the nepali word\n")
#MyDict.value("cloth")
#print(MyDict[Myword])
print("Meaning of your word",MyDict.get(Myword))#if we use MyDict.get() fuction then it gives "none " in place of invaliderror.