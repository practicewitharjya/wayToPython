# Passowrd should consist of  atleast 1 Upper, 1 lower, 1 spl char, 1 number
# Password should be minimum 8 char
import string
import random

passwordCombo1 = string.ascii_uppercase
passwordCombo2 = string.ascii_lowercase
passwordCombo3 = string.digits
passwordCombo4 = string.punctuation
finalComboList = list(passwordCombo1+passwordCombo2+passwordCombo3+passwordCombo4)
# print("Before Shuffle: ",finalComboList)

random.shuffle(finalComboList)
# print("After Shuffle: ",finalComboList)

passwdlength = int(input("Please enter the password length"))
passwdList = random.sample(finalComboList, passwdlength)
#print(passwdList)
passowrd = "".join(passwdList)
print(f"So your password is: {passowrd}")
