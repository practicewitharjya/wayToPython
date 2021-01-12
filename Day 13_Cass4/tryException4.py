try:
    num1 = int(input("Please enter a number"))
    num2 = int(input("Please enter another number"))
    print(num1/num2)

except ValueError:
    print("You have to enter an interger value")

except ZeroDivisionError:
    print("Don't provide 0, Try other number")

except:
    print("Something Went wrong")

# Only when the programme will run without any exception
else:
    print("You are in else part")

# Finally will be executed all the time
finally:
    print("You are in Finally block")