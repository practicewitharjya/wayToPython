# MultiLevel Inheritance

class GrandParent:
    name = 'Mr. Akhil Singh'
    sur_name = 'Sur'
    def grandParentFullName(self):
        print(f"{self.name} {self.sur_name}")

class Parent(GrandParent):
    name = 'Mr. Jashpreet Singh'
    def parentFullName(self):
        print(f"{self.name} {self.sur_name}")

class Me(Parent):
    name = 'Kamal'
    def myFullName(self):
        print(f"{self.name} {self.sur_name}")


kamal = Me()
kamal.myFullName()