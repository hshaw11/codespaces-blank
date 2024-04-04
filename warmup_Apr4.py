# In your own words describe what a Python While Loop is?
# A control flow statement which executes blocks of code.

# What does an iterator do in a Python Loop?
# It contains a countable numbers of values.

msg = 'hello' # variable called msg, being assigned
# the string value 'hello'
msg = 'goodbye'

while msg =='hello': # (so long as this is true) --
    # msg is equal to hello
    print(msg) # repeat this
msg = input('please enter a message: ')
if msg == 'goodbye':
    print("the loop has stopped! Congrats")