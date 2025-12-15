# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: crappo <crappo@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/09 12:55:07 by crappo            #+#    #+#              #
#    Updated: 2025/12/09 12:56:48 by crappo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	d1 = int(input("Day 1 harvest: "))
	d2 = int(input("Day 2 harvest: "))
	d3 = int(input("Day 3 harvest: "))
	print("Total harvest:", d1 + d2 + d3)