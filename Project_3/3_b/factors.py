# Author: Stanley Mpoyi
# Date: 03/25/2022
# Description: Program asks user to enter a number and
# prints out all the numbers that divide that integer evenly,
# including 1 and the number it's self.

number = int(input('Please enter a positive integer:  '))
print(f'The factors of {number} are: ')
for i in range(1, number+1):
    if number % i == 0:
        print(i)
