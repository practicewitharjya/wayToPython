# f = open("python.txt", "w")
# # f.write("It's a new file and I am using Python")
# f.write("It's a 2nd line")


f = open("python.txt", "a")
f.write("\nIt's a 3rd line and I am using append mode")

f.close()
