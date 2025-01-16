./tools/scripts/create_networks.sh

docker compose \
    -f $(pwd)/build/docker-compose/redis/docker-compose.redis.dev.yml \
    up \
    --build \
    --force-recreate \
    --remove-orphans \
