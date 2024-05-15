#You will use the next two weeks to design and develop a Python terminal program using all of the concepts you've learned throughout the semester.
#our program should include more than 1 python function to accomplish it's task and should also use a combnitation of data types, operators, and constructs.
#Your program should also include a python concept we haven't learned about in class (this can be somthing such as objects or built-in functions we did not discuss in class).
#You are permitted to work individually or in groups.

# BUDGET TRACKER APP

# BUDGET TRACKER APP PITCH
# In today's fast-paced world, managing personal finances can be a daunting task. From keeping track of expenses to budgeting for the future, it's easy to feel overwhelmed
# by the sheer amount of financial information we need to juggle. That's where the Budget Tracker App comes in - a powerful and user-friendly tool that helps you take control
# of your finances and achieve your financial goals. The Budget Tracker App is designed to be a comprehensive solution for individuals who want to better understand their
# spending habits, track their income, and maintain a healthy financial balance. Whether you're a young professional just starting out, a busy parent trying to manage
# a household budget, or a retiree looking to optimize your retirement savings, this app can provide the insights and tools you need to make informed financial decisions.
# One of the key features of the Budget Tracker App is it's intuitive and straightforward interface. Users can easily navigate through the app's menu options, allowing
# them to quickly add expenses, track their income, and view their overall budget.


# great project draft -> just break this down into 3 pargraphs - 1 paragraph is 3-4 sentence

# paragraph 1 - what is your idea?

# paragraph 2 -  what problem are you trying to sovle?

# paragraph 3 - who is your application designed for? 


# Finance tracker app 
# function 1 - add and withdraw money from account.
# function 2 - send money to another user.


# tools and context

# we need 3 functions:
# 1- add and withdraw money.
# 2 - send money from account to another person.
# 3 - a function that will hold the first 2. 

# we need to have a function that will represent the banking app. this function will contain the add/ withdraw function and the send money function.
# we will need a variable for the users account balance. This will be a float data type becuase it is a number. 
# we will need to have an input function that will let users pick what banking option they want to use. example: please select an option, add funds, withdraw, and transfer

# we need to create a function for adding money to account. 
# inside of the deposit/ add funds function, we need to take a number that the user inputs and add it to the account variable. We will use the addition arithmatic operator.

# we need to create a function for subtracting money from the account.
# inside of the withdraw/ subtraction funds function, we need to take a number that the user input and subtract that number from our account variable. We will us the subtraction arithmatic operator. 

# we need to create a funciton for removing and sending moneyt from the account. 

def  addMoney():
  print("Welcome to Haleems bank app")
  userAmount = input('how much money would you like to add')
  print(f'you have added {userAmount}')

addMoney()

def subtractmoney():
  print("welcome to Haleems bank app")
  userAmount = input('how much money would you like to subtract')
  print(f'you have subtracted {userAmount}')

def bankAppMain():
  print("Welcome to Haleems bank app")
  userAmount = input('how much money you got? ')
  print(f'you have {userAmount}')






bankAppMain()
