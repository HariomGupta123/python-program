class employee:
    company="google"
    def getsalary(self,signature):
        print(f"salary for working employee in {self.company} is {self.salary}\n{signature}")
    @staticmethod    
    def greet():
        print("good morning,sir")
        print("u r able")

hari=employee()
hari.salary=5000000
hari.getsalary("thanks")      
hari.greet()  