import random

#Return the next random floating point number in the range [0.0, 1.0).
# print(random.random())

#print(random.randint(1,100))
#print(random.randrange(0, 30, 5))

# brandList = ["Samsung", "LG", "MI", "APPLE"]
# print(random.choice(brandList))

# ludo = [1,2,3,4,5,6]
# print(random.choice(ludo))

numberList = [1,2,3,4,5,6,7,8,9]
random.shuffle(numberList)
print(numberList)
