# User variables
fizznum = 3
fizzword = "Fizz"
buzznum = 5
buzzword = "Buzz"
limit = 100


# Program

for i in range(limit):
    i = i + 1                                   # Start counting from 0
    if i % fizznum == 0 and i % buzznum == 0:   # Check for FizzBuzz
        print(fizzword + buzzword, end = '')    # Print FizzBuzz
    elif i % fizznum == 0:                      # Check for Fizz
        print(fizzword, end = '')               # Print Fizz
    elif i % buzznum == 0:                      # Check for Buzz
        print(buzzword, end = '')               # Print Buzz
    else:                                       # Check for neither
        print(i, end = '')                      # Print neither
    print(", ", end = '')                       # Print comma