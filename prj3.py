#project3: ROck paper scissors
import random

def computer_choice():
    options = ['rock','paper', 'scissors']
    return random.choice(options)

def human_choice():
    while True:
        choice = input("Enter rock, paper or scissors:")
        if choice.lower() in ['rock','paper','scissors']:
            return choice.lower()
        else:
            print("Invalid input, please try again.")

#human= human_choice()
#computer= computer_choice()

def compute_winner(human, computer):
    if human == computer:
        return "It is a tie!"
    elif human=='rock' and computer== 'paper':
        return "You loose!"
    elif human== 'paper' and computer== 'scissors':
        return "You loose!"
    elif human== 'scissors' and computer== 'rock':
        return "You loose!" 
    else:
        return "You win!"
    
def main():
    while True:
        human= human_choice()
        computer= computer_choice()
        result= compute_winner(human, computer)
        print(f"Your choice: {human}")
        print(f"Computer's choice: {computer}")
        print(result)
        play_game= input("Do you want to play again? (yes/no):")
        if play_game.lower() in ['yes', 'no']:
             play_game= play_game.lower()
        else:
            print("Invalid input, please try again.")
        if play_game== 'yes':
            continue
            continue
        elif play_game== 'no':
            print("Thanks for playing!")
            break
        
main()
