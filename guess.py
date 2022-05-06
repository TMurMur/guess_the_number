# Guess the Number game
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print(f"So, {myName.title()}, I guess the number from 1 to 20")

for guessesTaken in range(6):
    print("Try to guess")
    guess = int(input())

    if guess < number:
        print("Your number is small enough")
    elif guess > number:
        print("Your number is big enough")
    elif guess == number:
        break

if guess == number:
    guessesTaken = guessesTaken + 1
    print(f"Nice, {myName.title()}! You've managed in {guessesTaken} attempts!")

if guess != number:
    number = str(number)
    print("Unfortunately. I guessed the" + number + ".")