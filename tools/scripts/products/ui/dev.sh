#!/bin/bash

# command1 \
#   && command2 \
#   || command3 \
#   | command4

./tools/scripts/create_networks.sh

echo "Argument 1: $1"
PRODUCT_UI=$1
PRODUCT_UI_SERVICE="${PRODUCT_UI%%/*}"
echo "$first_word"

path=pymicroservicesbase/products/${PRODUCT_UI}

# .env.local becuase of nextjs
env_path=$(pwd)/pymicroservicesbase/products/${PRODUCT_UI}/.env.local

docker compose \
    -f $(pwd)/build/docker-compose/docker-compose.products.next.base.yml \
    -f $(pwd)/build/docker-compose/docker-compose.products.next.dev.yml \
    --env-file $env_path \
    -p ${PRODUCT_UI_SERVICE} \
    up \
    --build \
    --force-recreate \
    --remove-orphans \
    # -d

# docker compose \
#     -f $(pwd)/docker-compose/docker-compose.products.next.base.yml \
#     -f $(pwd)/docker-compose/docker-compose.products.next.dev.yml \
#     --env-file $env_path \
#     -p ${PRODUCT_UI_SERVICE} \
#     down \
#     -v \





# docker compose -f ./docker-compose/docker-compose.base.yml -f ./docker-compose/docker-compose.dev.yml --env-file ./environments/.env.development \
#     restart backend


# docker compose -f ./docker-compose/docker-compose.base.yml -f ./docker-compose/docker-compose.dev.yml --env-file ./environments/.env.development \
#    down -v
