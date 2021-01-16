def funargs(normal, *agrs):
    print("I am normal argument:",normal)
    for item in agrs:
        print(item)


nameList = ["Ayush", "Ishan", "Shyam"]
funargs("Papai", *nameList)