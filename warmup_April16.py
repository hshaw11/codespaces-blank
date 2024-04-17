# Warm up Tuesday April 16th, 2024.

import random

# 1. In your own words, explain the difference between an Python For Loop and a
# Python While Loop.

# For loops is used when the number of iterations is known and While loops will loop the statement in the program until it is proved right.

# 2. Create a loop that will iterate over a list of numbers. For evey number in your loop,
# it should multiply that number by 3. 

# Clues and keywords = loop; for loop to iterate over numbers.
# everytime or loop lands on a number- multiply by 3.
# list of numbers

def numberLoop():
    numberList = [1,2,3,4,5,6,7]
    for number in numberList: # for every item in this list ...
        print(number *3) # multiply that item by 3 ...

# 3. Use the following code snippet below to create a guessing game function. 
# The code below will generate a random number for you. You must write a loop that will
# ask the user to input their guess, if they guess incorrectly, the program will repeat 
# itself and ask the user to guess again. The program should continue to ask them to
# guess until they've gotten it correctly. Once they guess the correct number the program
# will congratulate them and the loop will stop. 

# generates a random number between 1 and 10
randomNumber = random.randint(1, 10)
print('Random number value is: {randomNumber}')

# clues
# program will repeat itself; if
# the number is not the correct guess.
# we'll need to create a function to store it.
# we'll use the input to take the users guess.

def guessingGame():
    randomNumber = random.randint(1, 10)
    print(f'Random number value is: {randomNumber}')
    i = int(input('please guess a number:'))

    while i != randomNumber:
        print('incorrect guess. Try again.')
        i = int(input('Please guess another number:'))

guessingGame()