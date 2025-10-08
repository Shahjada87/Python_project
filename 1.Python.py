
# # print("My name is "+input("WHat is your name?") )




# name = "Shahjada"
# print(len("1234556"))


# print(int("123") + int("123"))

# name_of_the_person = input("what is your name")
# length_of_name = len(name_of_the_person)
# print("number of letter in your name :" + str(length_of_name))


print("Welcome to the tip calculator!")
bill = float(input("What is the bill? $"))
tip = int(input("How much percentage tip would you like to give? 10 12 15"))
people =  int(input("How much people would you like to split? "))
bill_total = tip / 100 * bill + bill
per_person  = round(bill_total / people,2)
print("Each person should pay : " + str(per_person))
