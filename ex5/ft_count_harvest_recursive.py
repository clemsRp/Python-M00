# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: crappo <crappo@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/09 13:12:03 by crappo            #+#    #+#              #
#    Updated: 2025/12/15 10:45:58 by crappo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def count_recursive(days):
	if days > 1:
		count_recursive(days - 1)
	if days > 0:
		print("Day", days)

def ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	count_recursive(days)
	print("Harvest time!")