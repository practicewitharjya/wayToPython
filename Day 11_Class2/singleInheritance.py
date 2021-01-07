#Inheritance
# Classes can inherit the characteristics of other classes
# In below example we are doing Single inheritance where
# 2 methods will be inherited from Parent class to Child Class

class Parents:
    def growth(self):
        print("Growth is very good")

    def strength(self):
        print("Strength is good")

# Inherit a child class from Parent
class Child(Parents):
    def gender(self):
        print("It is a female baby")

    def little(self):
        print("It is a little baby")

newBornBaby = Child()
newBornBaby.gender()
newBornBaby.growth()