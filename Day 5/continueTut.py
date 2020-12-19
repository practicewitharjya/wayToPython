empList= {"Ayush": 10, "Papai": 8, "Shyam": 4, "Lily":10, "Popy": 14}
# Continue - To skip a particular value

for emp in empList:
    if emp == "Shyam":
        print("Don't provide any further leave")
        continue
    else:
        print(f"{emp}: You can take leave")
