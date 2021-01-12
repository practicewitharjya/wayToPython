class Employee:
    __empID = 0

    def setEmpID(self, empid):
        self.__empID = empid

    def getEmpID(self):
        return self.__empID


aysuh = Employee()
aysuh.setEmpID(12923)
print("Emp ID of Ayush is",aysuh.getEmpID())