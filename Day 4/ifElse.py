# Nested If

num = int(input("Enter a number of your choice: "))
# Is it divisible by 5? and is it divisble by 10 also?
if num%5 == 0:
    if num%10 == 0:
        print("This number is divisble by both 10 and 5")
    else:
        print("This number is only divisible by 5")
else:
    print("This is not divisible by both 5 and 10")

