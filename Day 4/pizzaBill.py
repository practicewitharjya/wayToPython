# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

finalbill = 0

if size == "S":
    finalbill=finalbill+100  #100
elif size == "M":
    finalbill=finalbill+200 #200
elif size == "L":
    finalbill = finalbill + 300  # 300

#Write your code below this line 👇



print(f"Your final bill is {finalbill}")