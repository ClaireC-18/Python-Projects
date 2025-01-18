#Function to get the Players choice for game
def get_player_choice():
    #Input function to get the Players choice
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    #Validate the input until a valid choice is provided
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return choice

#Function to randomise the computers choice for game
def get_computer_choice(): 
    import random
    #List of all possible choices for the computer's choice. Randomly select one. 
    choices = ['rock', 'paper', 'scissors']
    #Return the randomly selected choice from the choices list.
    return random.choice(choices)

#Function to determine the winner of the game based on the choices made by the player and computer.
def determine_winner(player_choice, computer_choice):
    #Check the choices and determine the winner based on the rules of the game.
    if player_choice == computer_choice:
        return "It's a tie!"
    #Check the choices and determine the winner based on the rules
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "Player wins!"
    else:
        return "Computer wins!"

#Main game loop
player_choice = get_player_choice()
print(f"You chose {player_choice}")
computer_choice = get_computer_choice()
print(f"Computer chose {computer_choice}")

winner = determine_winner(player_choice, computer_choice)
print(f"Computer chose {winner}")
