# f = open("codehub.txt")
# content = f.read()
# print(content)

# f = open("codehub.txt", "r")
# content = f.read()
# print(content)

# f = open("codehub.txt")
# content1 = f.read(10)
# print(content1)
# content2 = f.read(15)
# print(content2)
# content3 = f.read(16)
# print(content3)

# f = open("codehub.txt")
# for content in f:
#     print(content,end="")

# f = open("codehub.txt")
# content = f.readline()
# print(content)
# content2 = f.readline()
# print(content2)


f = open("codehub.txt")
content = f.readlines()
print(content)

# f = open("codehub.txt", mode='r', encoding='utf-8')

f.close()