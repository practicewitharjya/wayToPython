# mapping operator to function:  https://docs.python.org/3/library/operator.html

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

    # Operator Overloading
    # Dunder Method or Double Under method or Magic method
    def __add__(self, other):
        return self.salary+other.salary

    def __truediv__(self, other):
        return self.salary/other.salary

    def __mul__(self, other):
        print("Here I am doing Operator overloading of a * b")
        return None  # Without the return statement also by default None will be returned

ayush = Employee("Ayush Sharma","XYZ", 2000)
shyam = Employee("Shyam Goel","XYZ", 3000)
rohit = Employee("Rohit Roy","RBC", 5000)

# print(ayush+shyam)
# print(ayush/shyam)
print(ayush*shyam)

