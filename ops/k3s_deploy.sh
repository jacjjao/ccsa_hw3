#!/bin/bash

BASEDIR=$(dirname $(dirname $0))/k3s_yaml
sudo kubectl apply -f $BASEDIR/frontend_ingress.yaml
sudo kubectl apply -f $BASEDIR/frontend.yaml
sudo kubectl apply -f $BASEDIR/backend.yaml
sudo kubectl apply -f $BASEDIR/db_secrets.yaml
sudo kubectl apply -f $BASEDIR/database.yaml