# Author: Stanley Mpoyi
# Date: 03/25/2022
# Descriotion: The program takes the time in seconds as an argument.
#  The function returns the distance in meters that the object has
# fallen in that time.


def fall_distance(secs):
    """The function takes in secs as argument and returns the distance
    the object has fallen in meters """

    return (1/2) * 9.8 * (secs ** 2)
