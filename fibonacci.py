# User variables
limit = 100


# Program

num1 = 0
num2 = 0
temp = 0

while num1 < limit:

    if num2 == 0:                           # Special case for if num2 == 0
        print(str(num2) + ", ", end = '')
        num2 = num2 + 1
    if num2 > 0:                            #   Main code
        print(str(num2) + ", ", end = '')   # Print current num2 before starting operations
        temp = num2                         # Save away num2 for later
        num2 = num1 + num2                  # Make num2 the result of the addition of num1 and itself
        num1 = temp                         # Make num1 the previous version of num2