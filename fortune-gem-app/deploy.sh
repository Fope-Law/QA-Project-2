#!/bin/bash

# Build server
docker build -t fortune_gem_server server

# Build fortune-api
docker build -t yinyang_api yinyang_api


# Create network
docker network create fortune_gem_network

# Run containers
docker run -d -p 2020:2020 \
    --name fortune_gem_server \
    --network fortune_gem_network \
    fortune_gem_server

docker run -d \
    --name yinyang_api \
    --network fortune_gem_network \
    yinyang_api
