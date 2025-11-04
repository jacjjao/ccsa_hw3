#!/bin/bash

sudo docker service create --name registry --publish published=5000,target=5000 registry:2
sudo docker compose build
sudo docker compose push
sudo docker stack deploy -c docker-stack.yml app