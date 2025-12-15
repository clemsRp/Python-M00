# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: crappo <crappo@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/15 09:34:55 by crappo            #+#    #+#              #
#    Updated: 2025/12/15 10:45:01 by crappo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(item: str, quantity: int, unit: str) -> None:
	final_unit = ""
	if unit == "packets":
		final_unit = "packets available"
	elif unit == "grams":
		final_unit = "grams total"
	elif unit == "area":
		final_unit = "square meters"
	else:
		print("Unknown unit type")
	if final_unit == "square meters":
		print(f"{item[0].upper()}{item[1:]} seeds: covers {quantity} {final_unit}")
	elif final_unit != "":
		print(f"{item[0].upper()}{item[1:]} seeds: {quantity} {final_unit}")