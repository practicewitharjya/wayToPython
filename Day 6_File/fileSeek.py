#Seek

f = open("python.txt")

print(f.read(16))
print("After reading, position is: ",f.tell())
f.seek(2)
print(f.read(10))
print("After 2nd reading, position is: ",f.tell())

f.close()

