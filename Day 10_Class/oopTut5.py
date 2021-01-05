class Employee:
    def __init__(self, name, company, salary):
        self.name = name
        self.company = company
        self.salary = salary

    def employeeDetails(self):
        print(f"Employee name is {self.name}")


    def getEmpHike(self, hikeper):
        self.hikeper = hikeper
        self.finalSal = self.salary+(self.salary*self.hikeper)//100
        return self.finalSal


ayush = Employee("Ayush Sharma","XYZ", 2000)
ayush.employeeDetails()
salary = ayush.getEmpHike(20)
print("Final salary after hike is",salary)

