# import random

# A list of words that 
# potential_words = ["example", "words", "someone", "can", "guess"]

# word = random.choice(potential_words)

secret_word = "sandy"
# Use to test your code:
# print(secret_word)

# Converts the word to lowercase
secret_word = secret_word.lower()

# Make it a list of letters for someone to guess
current_word = ["_", "_", "_", "_", "_"] # TIP: the number of letters should match the word

# Some useful variables
guesses = ["_"]
maxfails = 7
fails = 0
guesses = guesses * len(secret_word  )

while fails < maxfails:
    guess = input("Guess a letter: ")
    guesses.append(guess)
    if guess in word:

    else
        print(guess)
	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

	print(current_word)

	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")
