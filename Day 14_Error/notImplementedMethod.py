class UPI:
    def sendMoney(self):
        raise NotImplementedError("You must have to implement in child class")
    def receiveMoney(self):
        raise NotImplementedError("You must have to implement in child class")

class PhonePe(UPI):
    def acceptMoney(self):
        pass
    def sendMoney(self):
        print("I have send Money feature")


ayush = PhonePe()
ayush.sendMoney()