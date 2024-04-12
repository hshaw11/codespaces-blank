# In your own words, describe the difference between a for loop and a while loop.
# For loops is used when the number of iterations is known and While loops will loop the statement in the program until it is proved right.

# Provide a scenario where you would use each of these constructs in a unique way.
# What is the best/ ideal scenario for using a for loop and what is the best/ ideal way of using a while loop?
# The best scenario for using a 'for' loop is when lterating over a sequence with a known end point, such as adding up even numbers in a list.
# The ideal way of using a while loop is when executing a block of code as long as a certain condition is true, such as repeatedly asking for user input until a specific
# value is entered.

# Best way to use for loop =
militaryTime =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

for hour in militaryTime:
    if hour == 5:
        print('sound the alarm')