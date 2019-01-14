git fetch --all
git checkout 7.1.x
docker-compose up -d

container_id=`docker ps | grep "dockercomposelamp_mysql" | awk '{print $1}'`
docker exec -it $container_id sh
