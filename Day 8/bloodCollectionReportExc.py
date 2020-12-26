"""
we have to define 2 functions
1. sendMail()  -- this will send the online report to customer
2. sendCourier() -- send hard copy to customer

I will take input from user:
 Press 1 to receive online report
 Press 2 to recive hard copy

if userinput is 1:
    sendMail(mailid)
if userinput is 2:
    sendCourier(address,pincode)
"""
def sendMail(mailid):
    print(f"Mail has been sent to {mailid}")

def sendCourier(address,pincode):
    print(f"Your report will be dispatched to {address} & area pincode: {pincode}")


print("Do you want Online report or Hard copy?")
userInput = input("Type: Soft copy  or Hard copy").casefold()

if userInput == "soft copy":
    mailid = input("Please enter your mail id")
    sendMail(mailid)
elif userInput == "hard copy":
    address = input("Please enter your addess")
    pin = int(input("Please enter your Area pin code"))
    sendCourier(address, pin)
else:
    print("You have entered a wrong input")

