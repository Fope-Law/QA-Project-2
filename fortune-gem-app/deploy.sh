#!/bin/bash

# Build server
docker build -t fortune-gem_server server

# Build fortune-api
docker build -t fortune_api fortune_api

# Build gem-api
docker build -t gem_api gem_api

# Create network
docker network create fortune-gem_network

# Run containers
docker run -d -p 2020:2020 \
    --name fortune-gem_server \
    --network fortune-gem_network \
    fortune-gem_server

docker run -d \
    --name fortune_api \
    --network fortune-gem_network \
    fortune_api

docker run -d \
    --name gem_api \
    --network fortune-gem_network \
    gem_api
