#!/bin/bash

# command1 \
#   && command2 \
#   || command3 \
#   | command4

# ./tools/scripts/products/ui/dev.sh demo_product/frontend/web/client
./tools/scripts/create_networks.sh

echo "Argument 1: $1"
WEB_SERVICE=$1


env_path=$(pwd)/pymicroservicesbase/services/${WEB_SERVICE}/.env

docker compose \
    -f $(pwd)/build/docker-compose/docker-compose.web_service.python.base.yml \
    -f $(pwd)/build/docker-compose/docker-compose.web_service.python.dev.yml \
    --env-file $env_path \
    -p ${WEB_SERVICE} \
    up \
    --build \
    --force-recreate \
    --remove-orphans \


# docker compose -f ./docker-compose/docker-compose.base.yml -f ./docker-compose/docker-compose.dev.yml --env-file ./environments/.env.development \
#     restart backend


# docker compose -f ./docker-compose/docker-compose.base.yml -f ./docker-compose/docker-compose.dev.yml --env-file ./environments/.env.development \
#    down -v
