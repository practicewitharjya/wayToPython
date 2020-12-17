# Red zone = "There is a complete lockdown"
# Orange zone = "Conditional movement"
# Green Zone = "Free movement"

areazone = input("Which zone you are from?")
if areazone == "redzone":
    print("There is a complete lockdown")

elif areazone == "orangezone":
    print("Conditional movement")

elif areazone == "greenzone":
    print("Free movement")

else:
    print("Your Zone is not listed in Govt site")