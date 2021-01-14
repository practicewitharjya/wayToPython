class Phone:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    #Abstract Method
    def mobileName(self):
        raise NotImplementedError("You have to implement this in child class")

class SmartPhone(Phone):
    def __init__(self, brand, model, internal_memory):
        super().__init__(brand, model)
        self.internal_memory = internal_memory

    def mobileName(self):
        return f"{self.brand}: {self.model}"

s11 = SmartPhone("Samsung","S11","64 GB")
print(s11.mobileName())