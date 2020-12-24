countryList = ["US", "India", "UK", "Russia", "Japan", "China", "Malaysia"]

for count,item in enumerate(countryList, 1):
    if item == "Russia":
        print(f"Russia is in {count}th position")

tuple1 = ("US", "India", "UK")
for count,item in enumerate(tuple1, 1):
    if item == "India":
        print(f"India is in {count}th position")

string1 = "India Is A country"
print(list(enumerate(string1)))