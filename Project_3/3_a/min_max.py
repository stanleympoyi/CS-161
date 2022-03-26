# Author: Stanley Mpoyi
# Date: 03/25/2022
# Description: Program asks user how many numbers
# user wishes to enter, accepts postive integer.
# program returns the minimun number and maximum number


print("How many integers would you like to enter? ")

number = int(input())

print(f'Please enter {number} integers')
# we assign the first input to min and max
min_num = int(input())
max_num = min_num
# loop through until condition becomes falls
while number-1:
    input_num = int(input())
    # if new input is greater than previous input, max is new input
    if max_num < input_num:
        max_num = input_num
    # if new input is less than previous input, min is new input
    elif min_num > input_num:
        min_num = input_num
    number -= 1
print(f'min: {min_num}')
print(f'max: {max_num}')
