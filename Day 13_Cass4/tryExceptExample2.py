while True:
    try:
        age = int(input("Please enter your Age"))
        break
    except ValueError:
        print("You have to enter an interger value")
    except:
        print("Something Went wrong!!!")

if age < 18:
    print("You can't vote")
else:
    print("You can vote")