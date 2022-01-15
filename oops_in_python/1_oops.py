class transportForm:
    formtype = "transport"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Bus is {self.bus}")

    

harisapplication = transportForm()
harisapplication.name="hari"
harisapplication.bus="pokhara-Butwal"
harisapplication.printData()
