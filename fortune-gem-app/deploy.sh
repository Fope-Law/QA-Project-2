#!/bin/bash

project_name = fortune-gem

# Build server
docker build -t $(project_name)_server server

# Build fortune-api
docker build -t $(project_name)_api fortune-api

# Create network
docker network create $(project_name)_network

# Run containers
docker run -d -p 2020:2020 \
    --name $(project_name)_server \
    --network $(project_name)_network \
    $(project_name)_server

docker run -d \
    --name $(project_name)_api \
    --network $(project_name)_network \
    $(project_name)_api
