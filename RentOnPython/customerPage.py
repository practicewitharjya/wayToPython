from RentOnPython.commonUtil import CommonUtil
class Customer:

    def doRegisterAnewCustomer(self):
        self.customerName = input("Enter your Name: ")
        self.mailID= input("Enter your mailID: ")
        self.username = input("Please enter a username: ")
        self.password = input("Enter a password: ")
        print("Congratulations your Account has been created!!!!")
        CommonUtil.sendMail(self.mailID, "Congratulations your Account has been created!!!!",
                            f"Welcome {self.customerName} to RentOnPython")

    def login(self, username, password):
        if self.username == username and self.password == password:
            return True
        else:
            return False
