
def ft_count_harvest_iterative():
    '''
    Count iteratively the number of days since harvest
    '''
    days = int(input("Days until harvest: "))
    for k in range(days):
        print("Day", k + 1)
    print("Harvest time!")
