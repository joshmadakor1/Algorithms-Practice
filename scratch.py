resultValue = 0  # Create a variable called "resultValue" and set it to 0
firstValue = 0   # Create a variable called "firstValue" and set it to 0
secondValue = 0  # Create a variable called "secondValue" and set it to 0

firstValue = input()  # Type a number at the command prompt and press enter, it will go in here
secondValue = input() # Same as above line

# 'int()' attempts to force whatever is in the () to become a number
# 'secondValue' is subtracted from 'firstValue' (the things you entered on the command line)
# the result is stored in 'resultValue'
resultValue = int(firstValue) - int(secondValue) 

# "Result: " is printed to the console
print("Result: ")

# whatever the value of 'resultValue' is, is printed to the console
print(resultValue)