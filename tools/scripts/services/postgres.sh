./tools/scripts/create_networks.sh

docker compose \
    -f $(pwd)/build/docker-compose/postgres/docker-compose.postgres.dev.yml \
    up \
    --build \
    --force-recreate \
    --remove-orphans \
