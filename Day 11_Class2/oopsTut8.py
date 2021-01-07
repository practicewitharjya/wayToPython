class College:
    clgName = "Horizon college"
    noOfSubject = 0

    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

    #Class Method
    @classmethod
    def changeCollegeName(cls):
        cls.clgName = "Modern College"

    #Instance Method
    def semesterExam(self):
        return f"You have to give exam for {self.dept}"

    #Static Method
    @staticmethod
    def collegeProgram():
        print("Every year we will celebrate.")


student1 = College("Ram", 21, "ECE")
student2 = College("Shyam", 22, "CSE")
professor = College("Dr. Saikat", 45, "IT")

College.changeCollegeName()
# Calling Class Method using Classname
print("Now the college name is",College.clgName)
# Calling Instance Method using object
print(student1.semesterExam())
# Calling Static Method using Classname
College.collegeProgram()