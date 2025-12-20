#!/usr/bin/env python3

def ft_water_reminder():
    '''
    Display a message depending on the last watering of the plant
    '''
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
