import random

print("Welcome to Bagram 21 Number Game!")
position = input('Do you want to go First or Second? \n "F" for First \n "S" for Second\n').upper()
numbers = []  # List to keep track of numbers played

while len(numbers) < 21:
    if position == "F":
        # Player's turn
        print("How many numbers do you wish to enter?")
        num_of_numbers = int(input())  # Ask the player how many numbers to play

        for _ in range(num_of_numbers):
            if len(numbers) < 21:  # Ensure numbers do not exceed 21
                next_number = len(numbers) + 1  # Determine the next number to append
                numbers.append(next_number)
                print(f"You played: {next_number}")
        
        print("Numbers after your turn:", numbers)

        if len(numbers) >= 21:  # Check if the game ends after the player's turn
            print("YOU LOSE.\nBetter luck next time!")
            break

        # Computer's turn
        computer_count = random.randint(1, 3)  # Randomly choose how many numbers the computer plays
        for _ in range(computer_count):
            if len(numbers) < 21:  # Ensure numbers do not exceed 21
                next_number = len(numbers) + 1
                numbers.append(next_number)
                print(f"Computer played: {next_number}")
        
        print("Numbers after computer's turn:", numbers)

        if len(numbers) >= 21:  # Check if the game ends after the computer's turn
            print("COMPUTER LOSES. Congratulations, you win!")
            break

    elif position == "S":
        # Computer's turn
        computer_count = random.randint(1, 3)  # Randomly choose how many numbers the computer plays
        for _ in range(computer_count):
            if len(numbers) < 21:  # Ensure numbers do not exceed 21
                next_number = len(numbers) + 1
                numbers.append(next_number)
                print(f"Computer played: {next_number}")
        
        print("Numbers after computer's turn:", numbers)

        if len(numbers) >= 21:  # Check if the game ends after the computer's turn
            print("COMPUTER LOSES. Congratulations, you win!")
            break

        # Player's turn
        print("How many numbers do you wish to enter?")
        num_of_numbers = int(input())  # Ask the player how many numbers to play

        for _ in range(num_of_numbers):
            if len(numbers) < 21:  # Ensure numbers do not exceed 21
                next_number = len(numbers) + 1
                numbers.append(next_number)
                print(f"You played: {next_number}")
        
        print("Numbers after your turn:", numbers)

        if len(numbers) >= 21:  # Check if the game ends after the player's turn
            print("YOU LOSE.\nBetter luck next time!")
            break
