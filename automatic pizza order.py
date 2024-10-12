print("Thank you for choosing Python Pizza Deliveries..!")
prize = 0
size = input('What size pizza would you like? Type "S" for Small, "M" for Medium, or "L" for Large.\n= ')
if size.lower() == "s":
    prize = 15
elif size.lower() == "m":
    prize = 20
else:
    prize = 25
add_pepperoni = input("Do you want pepperoni? Y or N: ")
if add_pepperoni.lower() == "y":
    if size.lower() == "s":
        prize += 2
    elif size.lower() == "m" or size.lower() == "l":
        prize += 3
add_cheese = input("Do you want extra cheese? Y or N: ")
if add_cheese.lower() == "y":
    prize += 1 
print(f"Your Final Bill is: ${prize}")





