# Author: Stanley Mpoyi
# Date: 03/26/2022
# Descriotion: The program takes a positive integer parameter as the initial
#  number of a hailstone sequence and returns how many steps it takes
# to reach 1 If the starting integer is 1, the return value should be 0,

def hailstone(n):
    '''Function returns how many steps it took to return 1'''

    count = 0
    # check if number is 1 and returns 0
    if n == 1:
        return count
    # iterate until number is 1
    while n != 1:
        # check if number is even and divides it by 2
        if n % 2 == 0:
            n = n // 2
            count += 1
        elif n % 2 == 1:
            n = (n * 3) + 1
            count += 1
    return count


result = hailstone(1000)
print(result)
