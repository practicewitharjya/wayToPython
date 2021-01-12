# Multiple Inheritance

class Mom:
    def beatuful_eye(self):
        print("I have Beautiful eye.Coming from mom")

    def efficiency(self):
        print("This is mom's Efficiency")

class Dad:
    def preety_nose(self):
        print("I have preety nose,Coming from Dad")

    def efficiency(self):
        print("This is dad's Efficiency")

class Child(Dad, Mom):
    def study(self):
        print("Child is very good in Study: His own characteristics")

    # def efficiency(self):
    #     print("This is child's Efficiency")


ayush =  Child()
# ayush.preety_nose()
# ayush.beatuful_eye()
# ayush.efficiency()
# ayush.study()

ayush.growth()