"""
We can't update class variable using Object.
But if we need to update, we have to use the classname
"""
class Employee:
    # Class attribute/Class variable
    no_of_leaves = 10

# Creating object
ayush = Employee()
shyam = Employee()

# Accessing by classname
print("No of leaves for any Employee:",Employee.no_of_leaves)
# Accessing by Object
print("No of leaves for Ayush:",ayush.no_of_leaves)
ayush.no_of_leaves = 15
print("After changing no of leaves for Ayush:",ayush.no_of_leaves)
print("No of leaves for Shyam:",shyam.no_of_leaves)

Employee.no_of_leaves = 20
print("After changing no of leaves for Ayush:",ayush.no_of_leaves)
print("No of leaves for any Shyam:",shyam.no_of_leaves)

