# Parent class/Super class
class Person:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

#Child class/Sub class
class Employee(Person):

    def isEmployee(self):
        return True

ram = Person("Ram")
# print(ram.getName())
# Parent class object can't access child class methods
#print(ram.isEmployee())

ayush = Employee("Ayush")
print(ayush.getName())
print("Is Ayush Employee:",ayush.isEmployee())