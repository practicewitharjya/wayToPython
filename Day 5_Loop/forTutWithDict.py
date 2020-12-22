marksDict = {"Math": 100, "Phy": 90}

# To Fetch only Key
for key in marksDict:
    print(key)

# To Fetch only Values
for value in marksDict.values():
    print(value)

# To Fetch both Key and Values
for key, value in marksDict.items():
    print(key,'-->', value)