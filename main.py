
import random

def get_user_choice():
    while True:
        user = input("What is your choice - 'r' for rock, 's' for scissor, 'p' for paper: ").lower()
        if user in ['r', 's', 'p']:
            return user
        else:
            print("Invalid choice. Please enter 'r', 's', or 'p'.")

def determine_winner(player, opponent):
    if player == opponent:
        return "It's a Tie!"
    elif (player == 'r' and opponent == 's'):
        return f"You won! Rock crushes Scissors."
    elif (player == 's' and opponent == 'p'):
        return f"You won! Scissors cut Paper."
    elif (player == 'p' and opponent == 'r'):
        return f"You won! Paper covers Rock."
    else:
        return f"You lost. {player.capitalize()} does not beat {opponent.capitalize()}."

def play_again():
    return input("Do you want to play again? (y/n): ").lower() == 'y'

def rock_paper_scissors():
    while True:
        player = get_user_choice()
        choices = ['r', 's', 'p']
        opponent = random.choice(choices)

        print(f"Your choice is {player}")
        print(f"Opponent's choice is {opponent}")

        result = determine_winner(player, opponent)
        print(result)

        if not play_again():
            print("Thanks for playing! Exiting the game.")
            break

rock_paper_scissors()
