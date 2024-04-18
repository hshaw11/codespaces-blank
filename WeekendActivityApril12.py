# Create a new python document called weekendActivity_April_12.py and complete the 
# following questions. 

# This activity must be submitted no later than Sunday April 14th, by 11:59pm to be
# accepted. 

# 1. In your own words, describe the difference between a FOR loop and a WHILE LOOP

# 2. Why is it important to havve programs be able to repeat themselves? If necessary, 
# do research to assist with your answer- Please do not copy/paste a response, but rather
# express your answer IN YOUR OWN WORDS using complete sentences. 

# 3. Create a function that uses a loop over the alphabet and print every 5th letter. 
# Write down clues, keywords, and breakdown and explain how you would approach this problem 
# in order to get full credit. 

def alphabetLoop():
    alphabetList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    iterate = range(alphabetList[0],alphabetList[6],5)
    for letter in iterate:
        print(letter)

alphabetLoop()
 
# 4A. Use W3schools to learn about the range() function. Describe how what the range
# function is and how it works.  

# The range function returns a sequence of numbers, starting from 0 by default and increments by 1 and stops before a specified number.

#4B. Then, create a loop using the range function that will only print multiples of 3 between 1 and 30.

def multiply():
    multiplyBy3 = range(1,30)
    for number in multiplyBy3:
        print(number * 3)
multiply()