import random

counter = 1

print("Welcome to the Random Number Guessing Game!")
#Gets the range of numbers from the user for the computer to select a random number
minNum = int(input("What is the lowest number? "))
maxNum = int(input("What is the highest number? "))

# Generate a random number between the given range
randomNumber = random.randint(minNum, maxNum)

# Game is initialized
guess = int(input("I have selected a random Number!\nWhat is your guess? "))

# Keep asking for guesses until player guesses correctly or runs out of attempts
while counter < 10:
    # if guess is correct, print the result and end the game
    if  guess == randomNumber:
        print("Congratulations! You guessed the correct number.")
        print(f"The number was {randomNumber}.")
        print("You won the game!")
        break
    # if guess is lower than the random number
    elif guess < randomNumber:
        print("Sorry, your guess was too low.")
        print(counter)
        guess = int(input("What is your next guess? "))
        counter += 1
    # if guess is greater than the random number    
    elif guess > randomNumber:
        print("Sorry, your guess was too high.")
        print(counter)
        guess = int(input("What is your next guess? "))
        counter += 1

# Handle case where the player doesn't guess correctly in 10 attempts
if counter == 10 and guess != randomNumber:
    print("Sorry, you didn't guess the number in 10 attempts.")
    print(f"The number was {randomNumber}.")
    print("Better luck next time!")