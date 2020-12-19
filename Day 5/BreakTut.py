empList= {"Ayush": 10, "Papai": 8, "Shyam": 4, "Lily":10}


for emp in empList:
    if emp == "Shyam":
        print("Don't provide any further leave")
        break
    else:
        print(f"{emp}: You can take leave")
