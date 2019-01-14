#!/usr/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    docker_status                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kdefaoui <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/14 22:37:43 by kdefaoui          #+#    #+#              #
#    Updated: 2019/01/14 22:37:43 by kdefaoui         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess

status = subprocess.call(['docker', 'info'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if status == 0:
    subprocess.call(['sh', 'main_ins.sh']);
else:
    print('Docker is not installed OR is not Running.\n>>> Run Docker and Try Again.')
