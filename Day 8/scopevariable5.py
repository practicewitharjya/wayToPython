a = 10 # Global variable

# Do we have a way to update global variable inside a function?
def sum():
    global a
    a = 20  # This will not create a local varibale as I am using Global keyword
    # print(a)

def multi():
    print(a*a) # 20*20

print("Before function call a =", a)
sum()
print("After function call a =", a)
multi()