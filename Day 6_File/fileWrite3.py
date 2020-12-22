f = open("dev.txt", "w")
line1 = "I am a professional\n"
line2 = "I am a developer\n"
line3 = "I know Python"

f.writelines(line1+line2+line3)

f.close()
