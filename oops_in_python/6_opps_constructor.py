class employee:
    company="google"
    def __init__(self,name,salary,subunit,age):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        self.age=age
    def getdetial(self):
        print("this is created")
        print(f"emplofee name:{self.name}")
        print(f"emplofee salary:{self.salary}")
        print(f"emplofee working place:{self.subunit}")
        print(f"emplofee age:{self.age}")
    




hari=employee("hari",5555,"google",23)
hari.getdetial()