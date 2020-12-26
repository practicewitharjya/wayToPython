import string
import random

def passwordGen(length):
    passwordCombo1 = string.ascii_uppercase
    passwordCombo2 = string.ascii_lowercase
    passwordCombo3 = string.digits
    passwordCombo4 = string.punctuation
    finalComboList = list(passwordCombo1 + passwordCombo2 + passwordCombo3 + passwordCombo4)

    random.shuffle(finalComboList)

    passwdList = random.sample(finalComboList, length)
    passowrd = "".join(passwdList)
    return passowrd


passwdlength = int(input("Please enter the password length"))
print(f"Generated password is: {passwordGen(passwdlength)}")
