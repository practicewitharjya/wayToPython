class Employee:
    #Class variable
    no_of_leaves = 10

    #Instance Method
    def employeeDetails(self, name):
        self.name = name
        print(f"Employee name is {self.name}")

    # Instance Method
    def getEmpHike(self, sal, hikeper):
        self.sal = sal
        self.hikeper = hikeper
        self.finalSal = self.sal+(self.sal*self.hikeper)//100
        return self.finalSal


ayush = Employee()
salary = ayush.getEmpHike(2000, 10)
print("Salary is",salary)