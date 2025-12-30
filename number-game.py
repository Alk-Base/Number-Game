#Simple number game. Depends on three functions:
#1. A function for greetings, greeting()
#2. The difficulty selection function, difficulty()
#3. The gameplay() function
#Beginner project

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
def gameplay(chances_counter):
    mystery = random.randint(1, 100)
    chances_left = chances_counter

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
            print(f"Congratulations! You guessed the correct number in {chances_counter - chances_left}!")
            break

        if chances_left == 0 and guess != mystery:
            print(f"No more chances! The number was {mystery}. Better luck next time!")
            break

#Executes the difficulty() and gameplay() functions with a single call, accepting them as callback functions
#RETURN TO THIS LATER: Why isn't it executing the gameplay() function upon running? It skips straight to the repetition() function
def execute(exec_difficulty, exec_gameplay):
    chances = exec_difficulty()
    print(chances)
    exec_gameplay(chances)
    return chances

def repetition():

    while True:
        try:
            repeat_answer = input("Play again? Answer 'yes' or 'no': ").lower()
        except ValueError:
            print("Invalid input, type 'yes' or 'no'")

        if repeat_answer == "yes":
            execute(difficulty, gameplay)
        elif repeat_answer == "no":
            print("Thanks for playing! Goodbye")
            break
        else:
            print("Invalid input, type 'yes' or 'no': ")

#Function calls to start the game
greeting()
execute(difficulty, gameplay)
repetition()