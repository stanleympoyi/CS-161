# Author: Stanley Mpoyi
# Date: 03/26/2022
# Descriotion: The program takes a positive integer parameter and returns
#  the number at that position of the Fibonacci sequence.

# Function for nth fibonacci
# number - Space Optimisation
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
    '''The program will run the fibonnacci sequence'''
    a = 0
    b = 1

    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")

    # Check is n is equal
    # to 0
    elif n == 0:
        return 0

    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


# Driver Program
print(fibonacci(10))

# This code is contributed by Saket Modi
# Then corrected and improved by Himanshu Kanojiya
