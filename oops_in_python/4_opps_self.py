class employee:
    company="Gooogle"
    def getsalary(self):
       print(f"Salary for this employee working in {self.company} is {self.salary}")



hari=employee()
hari.salary=5000
hari.getsalary()