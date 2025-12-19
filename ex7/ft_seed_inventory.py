
def ft_seed_inventory(item: str, quantity: int, unit: str) -> None:
    '''
    Display the seed inventory passing in params
    '''
    final_unit = ""
    res = f"{item[0].upper()}{item[1:]} seeds: "
    if unit == "packets":
        final_unit = "packets available"
    elif unit == "grams":
        final_unit = "grams total"
    elif unit == "area":
        final_unit = "square meters"
    else:
        print("Unknown unit type")
    if final_unit == "square meters":
        res += "covers"
    if final_unit != "":
        res += f"{quantity} {final_unit}"
        print(res)
