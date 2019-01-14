#!/usr/bin/python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    start_mysql.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kdefaoui <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/14 22:56:27 by kdefaoui          #+#    #+#              #
#    Updated: 2019/01/14 22:57:23 by kdefaoui         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess

status = subprocess.call(['docker', 'info'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if status == 0:
    subprocess.call(['sh', 'mysql.sh']);
else:
    print('Docker is not Running.\n>>> Run Docker and Try Again.')
