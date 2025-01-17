def get_player_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice(): 
    import random
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "Player wins!"
    else:
        return "Computer wins!"

player_choice = get_player_choice()
computer_choice = get_computer_choice()
print(f"You chose {player_choice}")
print(f"Computer chose {computer_choice}")


winner = determine_winner(player_choice, computer_choice)
print(f"Computer chose {winner}")
