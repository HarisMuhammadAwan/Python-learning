#project 2: Number guessing game

import random

def num_guessing_game():
    Target_number = random.randint(1, 100)
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100:"))
            if(guess<1 or guess>100):
                print("Invalid input,")
            elif(guess==Target_number):
                print("Congratulations! You guessed the right number!")
                break
            elif(guess>Target_number):
                print("Too high!")
            elif(guess<Target_number):
                print("Too low!")
        except ValueError:
            print("Invalid input, please try again.")

num_guessing_game()