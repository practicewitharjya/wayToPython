x = 30  # 50

def home():
    x = 10 # Local variable
    def door():
        global x
        x = 50
    print("Before Door function call:", x) #10, #10
    door()
    print("After Door function call:", x)  #30, #50


home()
print("Outside of all functions:", x)


