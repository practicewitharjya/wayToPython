#Tell

f = open("python.txt")

print("Before start, position is: ",f.tell())
print(f.read(16))
print("After reading, position is: ",f.tell())
print(f.read(10))
print("After 2nd reading, position is: ",f.tell())

f.close()