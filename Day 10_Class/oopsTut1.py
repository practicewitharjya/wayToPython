"""
Class is a blueprint for any real world object
Object has 2 characteristics:
    a. attribute : Variable
    b. behaviour : Methods

DRY: Don't Repeate Yourself
"""
class Employee:
    pass

# Creating object
ayush = Employee()
shyam = Employee()
papai = Employee()

ayush.name = "Ayush Sharma"
ayush.company = "XYZ"
ayush.salary = 3000

shyam.name = "Shyam Goel"
shyam.company = "XYZ"
shyam.salary = 2000

papai.name = "Papai Sur"
papai.company = "ABC"
papai.salary = 2500
papai.skil = ["Java", "Python", "HTML"]


print(shyam.name)
print(papai.skil)






