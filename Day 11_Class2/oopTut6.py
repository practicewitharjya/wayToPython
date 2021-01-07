class Employee:
    # Class variable
    no_of_leaves = 10

    def __init__(self, name, company, salary):
        self.name = name
        self.company = company
        self.salary = salary

    # Instance method
    def employeeDetails(self):
        print(f"Employee name is {self.name}")

    # Instance method
    def getEmpHike(self, hikeper):
        self.hikeper = hikeper
        self.finalSal = self.salary+(self.salary*self.hikeper)//100
        return self.finalSal

    # Class Method
    # We have to use @classmethod decorator
    @classmethod
    def changeLeaves(cls):
        cls.no_of_leaves = 12
        return cls.no_of_leaves

    #Static method is bound to class, static method can't access or modify the class state
    @staticmethod
    def welcomeMethod():
        print("Welcome to our company!!!")


ayush = Employee("Ayush Sharma","XYZ", 2000)
shyam = Employee("Shyam Goel","XYZ", 3000)
rohit = Employee("Rohit Roy","RBC", 5000)

Employee.changeLeaves()
# print("No of leave for all Emp:",Employee.no_of_leaves)
# print("No of leave of Ayush:",ayush.no_of_leaves)
# print("No of leave of Rohit:",rohit.no_of_leaves)

Employee.welcomeMethod()

