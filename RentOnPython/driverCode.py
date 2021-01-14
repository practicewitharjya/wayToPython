from RentOnPython.customerPage import Customer
from RentOnPython.productPage import Product
userObj = Customer()
prod = Product()

userObj.doRegisterAnewCustomer()

print("Login with your credential......")
username = input("Enter Your login ID: ")
password = input("Enter Your login Password: ")

isLoginSuccess = userObj.login(username,password)
if isLoginSuccess == True:
    print("Login is Successfull")
    prod.displayProduct()
    choice = int(input("Press 1 to Rent\nPress 2 to Return a Product"))
    if choice == 1:
        item = input("What do you want to Rent?")
        if item in prod.productList:
            prod.rentAProduct(item)
        else:
            print("Please choose from the available Products")
    elif choice == 2:
        item = input("What do you want to return?")
        prod.returnProduct(item)
    else:
        print("Incorrect Input. You have to enter between 1 and 2.")

else:
    print("Incorrect Credential.")