# Hierarchical Inheritance

# Parent Class
class SweetFruit:
    taste = "Sweet"
    def getTaste(self):
        print(f"It tastes {self.taste}")

# 1st Child
class Apple(SweetFruit):
    color = "Red"
    def getDetails(self):
        print(f"Name= Apple\nTaste= {self.taste}\nColor= {self.color}")

# 2nd Child
class Orange(SweetFruit):
    color = "Orange"
    def getDetails(self):
        print(f"Name= Orange\nTaste= {self.taste}\nColor= {self.color}")

# 3rd Child
class Banana(SweetFruit):
    color = "Yellow"
    def getDetails(self):
        print(f"Name= Banana\nTaste= {self.taste}\nColor= {self.color}")


apple = Apple()
banana= Banana()
apple.getDetails()
banana.getDetails()