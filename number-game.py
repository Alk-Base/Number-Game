#Hi! If you're interested enough in reading this, just know this is my first ever project. 
#It's pretty simple, but I'm really doing this so I can go through the whole dev experience from developing to managing with Git and pushing to GitHub

import random

upper_limit = 100
lower_limit = 1
chances = 0

#Simple greeting
def greeting():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. You have a limited amoung of guesses")
    print("Please choose a difficuly level:")
    print("")
    print("1. Easy: 10 chances")
    print("2. Medium: 5 chances")
    print("3. Hard: 3 chances")

#Provides an input for the player to input their difficulty level before starting the game
def difficulty():
    while True:
        chosen_difficulty = input("Please choose a difficulty with the number of the difficulty: ")

        match chosen_difficulty:
            case "1":
                print("Great! You have chosen the Easy difficulty level")
                return 10
            case "2":
                print("Great! You have chosen the Medium difficulty level")
                return 5
            case "3":
                print("Great! You have chosen the Hard difficulty level")
                return 3
            case _:
                print("Please choose a number from 1-3 to define a difficulty")
        


#Main gameplay loop. Picks a random number, sets an internal variable chances_left equal to chances to keep track of how many chances you have left, and loops around.
#chances_left determines if you can't continue
def gameplay():
    mystery = random.randint(1, 100)
    chances_left = chances

    while chances_left > 0:
        try:
            guess = int(input("Enter a number: "))
        except ValueError:
            print("Not a valid input. Please enter a number.")
            continue

        if guess < lower_limit or guess > upper_limit:
            print(f"Please enter a number between {lower_limit} and {upper_limit}.")
            continue

        if guess > mystery:
            print(f"Incorrect! The number is less than {guess}")
            chances_left -= 1
            print(f"You have {chances_left} chances left")
        elif guess < mystery:
            print(f"Incorrect! The number is greater than {guess}")
            chances_left -= 1
            print(f"You have {chances_left} chances left")
        else:
            print(f"Congratulations! You guessed the correct number!")
            break

        if chances_left == 0 and guess != mystery:
            print(f"No more chances! The number was {mystery}. Better luck next time!")
            break




#Function calls to start the game
greeting()
chances = difficulty()
gameplay()