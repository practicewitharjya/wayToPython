class SweetFruits:
    taste = "Sweet"

    def getTaste(self):
        print(f"It tastes {self.taste}")

class Apple(SweetFruits):
    color = "Red"

    def getDetails(self):
        print(f"Name= Apple\nTaste= {self.taste}\nColor= {self.color}")


apple = Apple()
apple.getDetails()