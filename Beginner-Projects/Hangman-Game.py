import random

# Gets users name
name = input("What is your name? ")
print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

guessed_wrong = []
guessed_correct = []
counter = 1

guess = input("I have selected a random Word!\nWhat letter would you like to guess? ")

    # Keep asking for guesses until player guesses correctly or runs out of attempts
while counter < 10 and guess in word:
    # if guess is correct, print the result and end the game
    if  guess in word:
        print("That letter is corrrect!")
        guess = input("What is your next guess? ")
        guessed_correct.append(guess)
        break
    # if guess is lower than the random word
    elif guess != word:
        print("Sorry, your guess was incorrect.")
        guess = input("What is your next guess? ")
        counter += 1
        guessed_wrong.append(guess)
    elif len(guessed_correct) == len(word) :
        print("Congratulations! You guessed the correct word.")
        print(f"The word was {word}.")
        print("You won the game!")
        break

# Handle case where the player doesn't guess correctly in 10 attempts
if counter == 10:
    print("Sorry, you didn't guess the word in 10 attempts.")
    print(f"The word was {word}.")
    print("Better luck next time!")