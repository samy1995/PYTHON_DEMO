import math


print("------------------------------------------------------------------------")

print("## Emoji Converter ##")
message = input("Please Enter Your Message: ")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😒",
    ";)": "😉"
}
output =""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

print("------------------------------------------------------------------------")

print("## Dictionaries ##")
phone = input("Please Enter Your Phone Number: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8":"Eight",
    "9": "Nine",
    "0": "Zero"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

print("------------------------------------------------------------------------")

print("## Dictionaries ##")
customer ={
    "name": "Samkit Shah",
    "birthdate": "28-03-1995",
    "address": "Toronto"
}
print(customer.get("name"))

print("------------------------------------------------------------------------")

print("## Tuples ##")
# cannot change tuples
numbers = (1, 25, 16, 18, 52, 36)
print(numbers)

print("------------------------------------------------------------------------")

print("## List Methods ##")
numbers = [1, 25, 16, 18, 52, 36]
numbers.insert(3, 99)
numbers.append(123)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

print("------------------------------------------------------------------------")

print("## Maximum Number using LISTS ##")
numbers = [27, 3, 5, 9, 10, 18]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

print("## 2D List ##")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])

print("------------------------------------------------------------------------")

print("## Nested Loops ##")
for x in range(4):
    for y in range(3):
        print(f'{x},{y}')

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'X'
    print(output)
    #print('X' * x_count)

print("------------------------------------------------------------------------")

print("## For Loops ##")
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f' Total:{total}')

print("------------------------------------------------------------------------")

print("Car Game")
command = ""
started = False
while True:
    command = input("Please enter your command for the car ").lower()
    if command == "start":
        if started:
            print("The car is already  started!! You Dumb Fuck!!")
        else:
            started = True
            print("The car engine started. let's Go...!!!!!! ")
    elif command == "stop":
        if not started:
            print("The car is already Stopped!! Stupid Ass!!")
        else:
            started = False
            print("The car engine Stopped. Amazing Ride..!!")
    elif command == "help":
        print("""
Please enter any of the following commands to play the game
Start - To Start the car
Stop - To stop the car
Quit - To quit the game
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I didn't Understand ")

print("------------------------------------------------------------------------")

print("## Guess Game ##")
secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Please Guess the correct Number: "))
    guess_count += 1
    if guess == secret_number:
        print("Congratulations!! You Win!!")
        break
    else:
        print("Please Try one more time ")
else:
    print("Sorry!! You Lost :(")

print("------------------------------------------------------------------------")

print("## While Loop ##")
i = 1
while i <= 10:
    print(i)
    i += 1

i = 1
while i <= 7:
    print(i * '#')
    i += 1

print("------------------------------------------------------------------------")

print("## Weight Converter ##")
weight = input("Please Enter Your Weight")
unit = input("Please enter unit (L)bs or (K)g")
if unit.upper() == "K":
    weight_lbs = float(weight) / 0.45
    print("Your Weight will be  ", weight_lbs, "(L)bs.")
if unit.upper() == "L":
    weight_kg = float(weight) * 0.45
    print("Your Weight will be  ", weight_kg, " (K)g.")
else:
    print("Please enter the correct unit. ")
print("Done...!!")

print("------------------------------------------------------------------------")

print("## If Statements Task with logical operators ##")
# AND: both
# OR: at least one
# NOT: none
price = float(input("Please enter the price for the house"))
credit = float(input("Please enter the credit score"))
if price >= 1000000 and credit >= 750:
    down_payment = 0.1 * price
    print(f'Your down payment will be  ${down_payment}')
if price >= 1000000 and credit >= 650:
    down_payment = 0.15 * price
    print(f'Your down payment will be ${down_payment}')
else:
    down_payment = 0.2 * price
    print(f'your down payment will be ${down_payment}')
print("Done..!!")

print("## If Statements ##")
temperature = float(input("Please enter the temperature = "))
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's A Nice Day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's Cold")
print('Done')

print("------------------------------------------------------------------------")

print("## Math Functions ##")

x = 2.8
print(round(x))
print(math.ceil(2.9))
print(math.floor(2.9))

print("Addition")
num1 = float(input("Enter Number One = "))
num2 = float(input("Enter Number Two = "))
sum = num1 + num2
print("The Sum of Num1 and Num2  = "+str(sum))

print("------------------------------------------------------------------------")

print("## String Methods ##")
course = "Python Programming"
print(len(course))
print(course.upper())
print(course.lower())
# print(course.find())
# print(course.replace())
print("------------------------------------------------------------------------")

print("## Formatted Strings ##")
name = "Samy"
l_name = "Shah"
print(f'{name} {l_name} is learning python.')

print("------------------------------------------------------------------------")

print("## Weight Converter ##")
weight_lbs = input("What is your weight in lb ? ")
weight_kg = float(weight_lbs) * 0.45
print(weight_kg)

print("------------------------------------------------------------------------")

print("## Variables and Receiving inputs ##")
print("Hello ")
name = input("What is your name? ")
birth_year = input("What is your Birth Year? ")
age = 2020 - int(birth_year)
color = input("What color do you like ?")
print(name + " you are ", age, " years old and you like " + color + " color")

