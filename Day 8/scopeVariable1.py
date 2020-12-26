marks = 40  # Global Variable
# Python will give priority to Local variable
def student():
    num = 5     # Local variable
    marks = 90  # Local variable
    print("Num=",num)
    print("Student Marks=",marks)

def Employee():
    marks = 100  # Local variable
    print("Emp Marks=",marks)


student()
Employee()
print("Global marks=",marks)