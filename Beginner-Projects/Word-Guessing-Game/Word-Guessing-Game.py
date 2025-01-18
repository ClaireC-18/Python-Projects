import random

# Gets users name
name = input("What is your name? ")
print("Good Luck ! ", name)

# Array of words and selects a ramdom one
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

counter = 1

# Game is initialized
guess = input("I have selected a random Word!\nWhat is your guess? ")

# Keep asking for guesses until player guesses correctly or runs out of attempts
while counter < 10:
    # if guess is correct, print the result and end the game
    if  guess == word:
        print("Congratulations! You guessed the correct word.")
        print(f"The word was {word}.")
        print("You won the game!")
        break
    # if guess is lower than the random word
    elif guess != word:
        print("Sorry, your guess was incorrect.")
        guess = input("What is your next guess? ")
        counter += 1

# Handle case where the player doesn't guess correctly in 10 attempts
if counter == 10 and guess != word:
    print("Sorry, you didn't guess the word in 10 attempts.")
    print(f"The word was {word}.")
    print("Better luck next time!")