#multilevel inheritance oops in python
class friends:
    school="paradise"
    def gethobby(self):
        print("Playing cricket")
    def getsalary(self):
        print("Rs.5000 only ")
class teacher:
    school="HD"
    def gethobby(self):
        print("vollyball")
    def getsalary(self):
        print("Rs.7777only ")
class programmer:
    school="ramjanki"
    def gethobby(sel):
        print("coding")
    def getsalary(self):
        print("Rs.8888 only ")

a=friends()
print(a.school)
a.getsalary()
b=teacher()
print(b.school)
b.getsalary()
c=programmer()
print(c.school)
c.getsalary()
a.gethobby()
b.gethobby()
c.gethobby()
    