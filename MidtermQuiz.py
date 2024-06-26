# Midterm quiz. 
# Create a new python document called midtermquiz.py
# Complete the following questions.
# Once you have comepleted your quiz, commit and sync your work to your GitHub. 

#RULES
# This quiz is open book; you may use your notes, google (only if you are viewing arcticles about python), W3schools only. Any other website
# is prohibitied.
# No phones are allowed during the quiz. refusal to put away a phone will result in failure.
# There is no talking during the quiz. If you complete the quiz, notify the instructor that you
# have finished. Once that is done, you are free to use your device and browse the web quitely. 

# Good Luck

# 1. In your own words, describe what the difference
# between a function arguement and a function parameter.
# Write your response using complete sentences.

# A function parameter is what is inside the parentheses().
# A function argument is the information that is sent to the function when it is called for.

# 2. In your own words, describe what each of the following errors means.
# Write your response using complete sentences.

# syntax error - A syntax error are characters that are ment to be written in a certain language.
# type error - A type error is when a line of code is incorrect.
# name error - A name error is when a variable doesn't exist.

# 3. What function would I use if I wanted to convert an integer data type into 
# a string data type?

# I would use the str function.

# 4. What function would I use if I wanted to change a float data type into a 
# an integer data type?

# I would use the int function.

# 5. Describe three (3) Variable naming rules. Write your response in complete sentences. 

# A variable name cannot start with a number.
# A variable name must start with a letter or the underscore character.
# A variable name cannot be any of the python keywords.

# 6. Name the operator family each of these symbols are a part of 
# and describe how each of these sybmols are used. Write your response
# useing complete sentences. 

#symbols
# = , Assignment operator . This will assign a variable to a value.
# == , Comparison operator. Will evalute if two values are NOT the same
# =!

# Assignment Operator
# They are used to assign values to variables.

# 7. You have been hired as an engineer to develop a car speed detection system.
# the car company would like to create a function where if the user goes over a certain
# speed it will notify them to change gears. The client has provided you with the following
# guidelines on how they would like the gear system to work:
# if the driver is going over 20mph, alert the driver to shift to gear 1
# if the the driver is going over 30mph, alert the driver to shift to gear 2
# if the driver is going over 40mph, alert the driver to shift to gear 3
# if the driver is going over 70mph, alert the driver to shift back to gear 1.
# the client would like you to pass in the speed that the user is going as an argument. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

# 8. You have been hired as an engineer to develop a fitness meal plan program. 
# your function should take in two (2) arguements; the day of the week, and the time of the day.
# depending on the time of the day; either morning or afternoon, the meal plan will change. 
# the client has provided you with the following meal plan information
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

def mealPlan(dayOfWeek, timeOfDay):
    if dayOfWeek == 'mon' and timeOfDay=='morning':
        print('2 eggs and an apple')
    elif dayOfWeek == 'mon' and timeOfDay =='afternoon':
        print('bbq grilled chicken and broccoli')
def mealPlan(dayOfWeek, timeOfDay):
    if dayOfWeek == 'tue' and timeOfDay=='morning':
        print('2 eggs and an apple')
    elif dayOfWeek == 'tue' and timeOfDay =='afternoon':
        print('bbq grilled chicken and broccoli')
def mealPlan(dayOfWeek, timeOfDay):
    if dayOfWeek == 'wed' and timeOfDay=='morning':
        print('2 eggs and an apple')
    elif dayOfWeek == 'wed' and timeOfDay =='afternoon':
        print('bbq grilled chicken and broccoli')
def mealPlan(dayOfWeek, timeOfDay):
    if dayOfWeek == 'thur' and timeOfDay=='morning':
        print('2 eggs and an apple')
    elif dayOfWeek == 'thur' and timeOfDay =='afternoon':
        print('bbq grilled chicken and broccoli')
def mealPlan(dayOfWeek, timeOfDay):
    if dayOfWeek == 'fri' and timeOfDay=='morning':
        print('2 eggs and an apple')
    elif dayOfWeek == 'fri' and timeOfDay =='afternoon':
        print('bbq grilled chicken and broccoli')

# monday morning= 2 eggs and an apple
# monday afternoon= bbq grilled chicken and broccoli

# tuesday morning= oatmeal with strawberries and blueberries
# tuesday afternoon= baked chicken with kale

# wednesday morning= fruit salad
# wednesday afternoon= curry goat with rice and cabbage

# thursday morning= pancakes and turkey sausage
# thursday afternoon= eggplant pasta

# friday morning= steak and eggs
# friday afternoon= cheesburger and fries

# saturday morning= oatmeal
# saturday night= baked chicken with string beans

# sunday morning = oatmeal
# sunday night = steak and spinach

# 9. You have been hired as an enineer to develop a school to develop an academic honors system.
# the client would like to check if the user has gotten above an 85% overall grade or has
# has accomplished passing the SAT. The client would like you to pass this information in as
# arguements. If either of these situations are true the student has made the academic honors list
# if only passing the SAT is true, congratulate the user but inform them they did not make the list.
# if they only scored above 85%, congratulate the user but inform them they did not make the list.
# if none of the conditions are met, inform them to continue studying and try again next semester. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

#keywords and clue: function with arguments,
# conditional logic for if something is true
# logical operators to compare 2 conditions.
# 85 > and sat= true - honors
# 85 < and sat= true - good, but not honors
# 85 > and sat= false - good, but not honors
# 85 < and sat= false - try again

def honorsCheck(grade, sat):
    if grade >= 85 and sat:
        print('Congrats, you have made honors.')
    elif grade < 85 and sat:
        print('Congrats on your grade, however you did not make honors.')

# 10. Create a function that will check the temperature outside. If the user enters
# a number above 60 degrees it is warm outside, if the enter a number above 80 degrees it is hot outside.
# if the user enters a number below 50 degrees it is cold outside. and if the tempeature is above 50 degrees,
# tell the user it's not warm but it's also not too cold. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.
        
# key words and clues: function
# conditional logical to check for different temps
# 60 > = warm outside
# 80 > = hot outside
# 50 < = cold outside
# 50 > = not hot, not cold

def temperatureCheck():
    temp= input("what is the temperature outside?")
