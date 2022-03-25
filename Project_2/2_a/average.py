# Author: Stanley Mpoyi
# Date: 03/25/2022
# Description: The program will ask the user to enter five
# numbers and will output the average number

print("Please enter five numbers.")
num_1 = float(input())
num_2 = float(input())
num_3 = float(input())
num_4 = float(input())
num_5 = float(input())

# find the total number of all inputs
average = num_1 + num_2 + num_3 + num_4 + num_5

# divide the total by the number of inputs
average /= 5

print(f'The average of those numbers is: \n {average}')
