# In your own words, describe what a while loop is?
# A while loop is used to repeat a specific block of code an unknown number of times.

# Create a function that uses a while loop to determine if a user has typed in 
# the the correct word guess. If the user types in the wrong word, your program 
# should inform them that their guess was inccorect and to try again, but if the
# user guesses the word correctly, your program shoul tell the user they have 
# guessed correctly and have won the game, stopping the loop.

def guess_the_word():
    # Set the correct word
    correct_word=()

    #Initialize the user's guess
    user_guess=()

    # Use a while loop to keep asking the user for a guess until they get it right
    while user_guess.lower() != correct_word:
        user_guess = input()

        # If the user's is incorrect, tell them to try again
        if user_guess.lower() != correct_word:
            print()

    # If the user guesses the correct word, tell them they've won
    print()