# args: Non Keywrod Argument
# kwargs: Keyword Argument

def funcargs(name, *agrs, **kwargs):
    print("This is positional argument", name)

    for item in agrs:
        print(item)

    for key, value in kwargs.items():
        print(f"Key= {key}, Value= {value}")


nameList = ["Ayush", "Ishan", "Shyam", "Hiru", "Kuhu"]
marketDict = {"Ayush": "Engg", "Ishan": "Doctor", "Shaym": "Teacher"}
funcargs("Papai", *nameList, **marketDict)
