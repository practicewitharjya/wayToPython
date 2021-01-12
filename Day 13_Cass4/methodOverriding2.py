class Phone:
    parentClassVar = "I am super"
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def mobileName(self):
        return f"{self.brand}: {self.model}"

class SmartPhone(Phone):
    def __init__(self,brand,model,price,ram,internal_memory,rear_camera):
        super().__init__(brand, model, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def mobileName(self):
        super().mobileName()
        print(super().parentClassVar)
        return f"{self.brand}: {self.model}, {self.ram}, {self.rear_camera}"



phone = Phone('Nokia', 1100, 2000)
smart_phone = SmartPhone('OnePlus','8T',50000, '16 GB','128 GB', '32 MP')
print(smart_phone.mobileName())