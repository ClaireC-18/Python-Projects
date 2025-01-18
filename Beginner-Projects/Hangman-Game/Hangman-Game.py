import random

# Gets user's name
name = input("What is your name? ")
print("Good Luck ! ", name)

# List of words to choose from
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

guessed_wrong = []
guessed_correct = []
counter = 0  # Start counter at 0

# Display the initial state
print("I have selected a random Word!")
print(f"Current guess correct: {guessed_correct}")
print(f"Current guess wrong: {guessed_wrong}")

# Keep asking for guesses until player guesses correctly or runs out of attempts
while counter < 10:
    # Display the current state of the word
    current_state = ''.join([letter if letter in guessed_correct else '_' for letter in word])
    print(f"Current word: {current_state}")

    guess = input("What letter would you like to guess? ").lower()  # Get the guess and convert to lowercase

    # Check if the guess is valid (a single letter)
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue  # Skip the rest of the loop and ask for a new guess

    # Check if the guess has already been made
    if guess in guessed_correct or guess in guessed_wrong:
        print("You have already guessed that letter. Try again.")
        continue  # Skip the rest of the loop and ask for a new guess

    # If guess is correct
    if guess in word:
        print("That letter is correct!")
        guessed_correct.append(guess)
    else:
        print("Sorry, your guess was incorrect.")
        guessed_wrong.append(guess)
        counter += 1  # Increment the counter only for wrong guesses

    # Display current state
    print(f"Current guess correct: {guessed_correct}")
    print(f"Current guess wrong: {guessed_wrong}")

    # Check if the player has guessed all letters
    if all(letter in guessed_correct for letter in word):
        print("Congratulations! You guessed the correct word.")
        print(f"The word was {word}.")
        print("You won the game!")
        break  # Exit the loop if the word is guessed

# Handle case where the player doesn't guess correctly in 10 attempts
if counter == 10:
    print("Sorry, you didn't guess the word in 10 attempts.")
    print(f"The word was {word}.")
    print("Better luck next time!")