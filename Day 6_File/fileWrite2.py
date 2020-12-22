# Handle the file as read and write mode
f = open("python.txt", "r+")
f.write("I am writing some more line in same file")
print(f.read())