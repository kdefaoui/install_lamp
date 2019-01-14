# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    install_lamp.sh                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kdefaoui <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/01/14 19:19:36 by kdefaoui          #+#    #+#              #
#    Updated: 2019/01/14 22:54:03 by kdefaoui         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

login=`whoami`;
# configure Docker
if [ ! -h '/Library/Containers' ]
then
	mv /Library/Containers /Volumes/Storage/goinfre/$login
	ln -s /Volumes/Storage/goinfre/$login/Containers /Library/Containers	
fi

cd

if [ ! -h '.docker' ]
then
	mv .docker /Volumes/Storage/goinfre/$login
	ln -s /Volumes/Storage/goinfre/$login/.docker .docker
fi
# install LAMP
cd ~/Desktop
git clone https://github.com/sprintcube/docker-compose-lamp.git
cd docker-compose-lamp/
git fetch --all
git checkout 7.1.x
docker-compose up -d
