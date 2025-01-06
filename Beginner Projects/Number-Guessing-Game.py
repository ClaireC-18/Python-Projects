import random

counter = 1

print("Welcome to the Random Number Guessing Game!")
minNum = int(input("What is the lowest number? "))
maxNum = int(input("What is the highest number? "))

randomNumber = random.randint(minNum, maxNum)

guess = int(input("I have selected a random Number!\nWhat is your guess? "))
while counter < 10:
    if  guess == randomNumber:
        print("Congratulations! You guessed the correct number.")
        print(f"The number was {randomNumber}.")
        print("You won the game!")
        break
    elif guess < randomNumber:
        print("Sorry, your guess was too low.")
        print(counter)
        guess = int(input("What is your next guess? "))
        counter += 1
    elif guess > randomNumber:
        print("Sorry, your guess was too high.")
        print(counter)
        guess = int(input("What is your next guess? "))
        counter += 1
    elif counter == 10:
        print("Sorry, you didn't guess the number in 10 attempts.")
        print(f"The number was {randomNumber}.")
        print("Better luck next time!")
        break