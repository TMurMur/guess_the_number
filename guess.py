# Guess the Number game
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input(f"> ")
print(f"Nice to meet you, {myName.title()}!\n"
            "My name is Numberator!\nLet's play the game!\n")

flag = True

while flag == True:
    limit = random.randint(20, 25) # Max value in range of numbers    

    number = random.randint(1, limit)
    print(f"So, {myName.title()} I guess the number from 1 to {limit}")

    for guessesTaken in range(6):
        print("Try to guess")
        guess = int(input("> "))

        if guess < number:
            print("Your number is small enough")
        elif guess > number:
            print("Your number is big enough")
        elif guess == number:
            break

    if guess == number:
        guessesTaken = guessesTaken + 1
        print(f"Nice, {myName.title()}! You've managed in {guessesTaken} "
            "attempts!\n")

    if guess != number:
        number = str(number)
        print("Unfortunately. I guessed the " + number + ".\n")

    switch = input("Do you want to replay the game? (y/n)\n> ")

    if switch == 'y':
        flag = True
    elif switch == 'n':
        flag = False

print(f"\nThank you for the game, {myName.title()}!\n"
    "Come back soon!")