

print("Welcome to the python pizza deliveries.")

print("Small Pizza (S) = $20")
print("Medium Pizza (M) = $25")
print("Large Pizza (L) = $30")

size = str(input("What pizza size do you want? Reply with S, M or L!!"))
pepperoni = str(input("Peperoni or not. Y or N."))
extra_cheese = str(input("Extra Cheese or not. Y or N."))

bill = 0

if size == "S" or size == "s":
    bill += 20
elif size == "M" or size == "m":
    bill += 25
elif size == "L" or size == "l":
    bill +=30
else:
    print("You entered the wrong size. Please try again.")


if pepperoni == "Y" or pepperoni == "y":
    if size == "S" or size == "s":
        bill += 2
    else:
        bill += 3
if extra_cheese == "y" or extra_cheese == "Y":
    bill += 1


print(f"Your final bill is ${bill}")