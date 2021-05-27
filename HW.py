from pathlib import Path
path = Path()
for file in path.glob('*'):
    print(file)




import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())

import random
for i in range(7):
    print(random.randint(10, 20))




print("Packages")
from ecommerce import shipping
shipping.calc_shipping()

print("practice module")
import util
from util import find_max
numbers = [10, 20, 30, 50, 100, 255, 355, 455, 1, 88, 33]
print(max(numbers))



print("module")
import Converter
from Converter import kgs_to_lbs
from Converter import lbs_to_kgs
print(kgs_to_lbs(70))
print(lbs_to_kgs(155.55))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print("Draw")
    def move(self):
        print("Move")


point = Point(10, 20)
print(point.x)
try:
    age = int(input("how old are you?"))
    print(age)
except ValueError:
    print("Please enter numeric value only.")

print("parameter")

def greet_user():
    first_name = input("Your first name?")
    last_name = input("Your last name?")
    print(f'Hello {first_name} {last_name}...!!')

greet_user()
feel = input("How you doing today?")
print(f'{feel} oh that is amazing')
print("Good Bye..!!")
print("You have yourself a great day :)")
print("functions")


def greet_user():
    print("How Are You?")
    print("Welcome aboard..!!")


print("Hi there..!!")
greet_user()
print("Good Bye..!!")

print("Tuples Unpacking")
coordinates = [1, 2, 3]
x, y, z = coordinates
print(x, y, z)


print("Removing Duplicates")
numbers = [2, 3, 2, 5, 6, 5, 7, 9, 2, 1, 0]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
        uniques.sort()
print(uniques)


print("2D List")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for column in matrix:
    for items in column:
        print(items)
print(matrix)
print(matrix[1][1])
matrix[1][1] = 20
print(matrix)

print("Maximum Number")
numbers = [3, 5, 9, 10, 18]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

print("F challenge")
numbers = [1, 1, 1, 5]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)

print("Nested Loop Co-ordinates")
for x in range(3):
    for y in range (2):
        print(f"{x}, {y}")


print("Loop addition")
prices = [10, 20, 30, 40, 50]
total = 0
for price in prices:
    total += price
print(f"total:  {total}")


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
            print("The car engine started ")
    elif command == "stop":
        if not started:
            print("The car is already Stopped!! Stupid Ass!!")
        else:
            started = False
            print("The car engine Stopped")
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

print("Guess Game")
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

print("Hello ")
name = input("What is your name? ")
birth_year = input("What is your Birth Year? ")
age = 2020 - int(birth_year)
print("Your name is " + name + " and your age is ", age, " years.")

print("Addition")
num1 = float(input("Enter Number One = "))
num2 = float(input("Enter Number Two = "))
sum = num1 + num2
print("The Sum of Num1 and Num2  = "+str(sum))

print("Functions")
course = "I am learning python"
print(course.upper())
print(course)
print(course.find('y'))
print(course.replace('p', 'P'))
print(course.count('n'))
print('python' in course)


print("If Statements")
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


weight = float(input('Please enter your weight = '))
unit = input("(K)g or (L)bs ")
if unit == 'k' or unit == "K":
    converted = weight / 0.45
    print("Your weight in Lbs is " + str(converted))
elif unit == "L" or unit == "l":
    converted = weight * 0.45
    print("Your weight in Kg is " + str(converted))
else:
    print("Please enter K or L")

print("While Loop")
i = 1
while i <= 10:
    print(i)
    i += 1

i = 1
while i <= 5:
    print(i * '#')
    i += 1

names = ['John', 'Bob', 'Mosh', 'Sam', 'Mary']
print(names)
print(names[0])
print(names[-2])
names[0] = "Jon"
print(names[0:4])

print('Functions')
numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.insert(5, 6)
numbers.remove(1)
print(numbers)
print(7 in numbers)
print(len(numbers))
numbers.clear()
print(numbers)

print("For Loop")
numbers = [1, 2, 3, 4, 5]
for items in numbers:
    print(items)

print("While Loop")
numbers = [1, 2, 3, 4, 5]
i = 0
while i < (len(numbers)):
    print(numbers[i])
    i += 1

print("Range Function")
numbers = range(7)
print(numbers)
for number in numbers:
    print(number)

numbers = range(10, 100, 20)
for number in numbers:
    print(number)

for number in range(20, 100, 20):
    print(number)


