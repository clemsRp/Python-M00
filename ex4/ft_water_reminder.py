# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: crappo <crappo@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/09 13:07:01 by crappo            #+#    #+#              #
#    Updated: 2025/12/09 13:08:32 by crappo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
	days = int(input("Days since last watering: "))
	if days > 2:
		print("Water the plants!")
	else:
		print("Plants are fine")