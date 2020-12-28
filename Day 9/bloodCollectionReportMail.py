import smtplib

def sendMail(to_mail,sub,msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('practicewitharjya@gmail.com', 'Java@1234')
    server.sendmail('practicewitharjya@gmail.com', to_mail, f"Subject: {sub}\n\n{msg}")
    server.quit()

def sendCourier(address,pincode):
    print(f"Your report will be dispatched to {address} & area pincode: {pincode}")


print("Do you want Online report or Hard copy?")
userInput = input("Type: Soft copy  or Hard copy").casefold()

if userInput == "soft copy":
    mailid = input("Please enter your mail id")
    sendMail(mailid, "Here is your report", "You are all good")
elif userInput == "hard copy":
    address = input("Please enter your addess")
    pin = int(input("Please enter your Area pin code"))
    sendCourier(address, pin)
else:
    print("You have entered a wrong input")

