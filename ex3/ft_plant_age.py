#!/usr/bin/env python3

def ft_plant_age():
    '''
    Display a message depending on the plant age
    '''
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
