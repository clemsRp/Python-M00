#!/usr/bin/env python3

def ft_count_harvest_recursive(days=None):
    prev_days = days
    if prev_days is None:
        days = int(input("Days until harvest: "))

    if days > 1:
        ft_count_harvest_recursive(days - 1)

    if days > 0:
        print("Day", days)

    if prev_days is None:
        print("Harvest time!")
