# Author: Stanley Mpoyi
# Date: 03/25/2022
# Descriotion: The program that prompts the user for an integer that
# the player (maybe the user, maybe someone else) will try to guess.
# If the player's guess is higher than the target number, the program
# should display "too high" If the user's guess is lower than the target
#  number, the program should display "too low" The program should use
#  a loop that repeats until the user correctly guesses the number.
# Then the program should print how many guesses it took.

print('Enter a number for a player to guess. ')
secret_num = int(input())
print('Enter your guess')
guess = int(input())
num_guesses = 1

while guess != secret_num:
    if guess < secret_num:
        print('Too low - Try again.')
        num_guesses += 1
    elif guess > secret_num:
        print('Too high - Try again')
        num_guesses += 1
    guess = int(input())

print(f'You guessed it in {num_guesses} tries')
