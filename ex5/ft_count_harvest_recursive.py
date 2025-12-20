#!/usr/bin/env python3

def count_recursive(days):
    if days > 1:
        count_recursive(days - 1)
    if days > 0:
        print("Day", days)


def ft_count_harvest_recursive():
    '''
    Count recursively the number of days since harvest,
    using the count_recursive function
    '''
    days = int(input("Days until harvest: "))
    count_recursive(days)
    print("Harvest time!")
