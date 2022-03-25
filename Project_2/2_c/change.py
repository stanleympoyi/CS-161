# Author: Stanley Mpoyi
# Date: 03/25/2022
# Description: Program accepts amount less than a dollar
# and calculates how many Quarters, Nickels, Dimes and pennies
# makes up to the amount inputed.

print("Please enter an amount in cents less than a dollar.")

amount = int(input())

Quarter = 25
Dime = 10
Nickel = 5
Penny = 1

print('Your change will be.')

Q = amount // Quarter
amount %= Quarter
print(f'Q: {Q}')
D = amount // Dime
amount %= Dime
print(f'D: {D}')
N = amount // Nickel
amount %= Nickel
print(f'N: {N}')
P = amount // Penny
amount %= Penny
print(f'P: {P}')
