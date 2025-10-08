# # check a number is odd or even 

# num1 = int(input("Please enter a number = "))

# if num1 % 2 == 0:
#     print("The number is an even number.")
# else:
#     print("the number is an odd number.")






print("Welcome to the rollercoster!!")

height = int(input("What is your height? "))


if height >= 120:
    print("You are allowed to ride the rollercoster. But")
    age = int(input("Please let us know your age for a $5, $10 or $15 ticket! "))
    if age < 12 :
        bill = 5
        print("Child tickets are $5.")
    elif age >= 12 and age < 18:
        bill = 10
        print("Youth tickets are $10.")
    elif age >=18 :
        bill = 15
        print("Adult tickets are $15.")
    picture = input("Do you want photos? Please reply with Yes or No!!")
    if picture == "Yes" or picture == "yes":
        total_bill = bill + 3
        print("Your final bill is $" + str(total_bill))
    elif picture == "No" or picture == "no":
        total_bill = bill
        print("Thank you for riding. Your final bill is $" + str(bill))
else:
    print("Please grow little more taller to be able to ride the roller coster.")