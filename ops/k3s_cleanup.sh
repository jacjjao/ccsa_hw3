#!/bin/bash

sudo kubectl delete ingress frontend-ingress
sudo kubectl delete services frontend
sudo kubectl delete deployment frontend
sudo kubectl delete services backend
sudo kubectl delete deployment backend
sudo kubectl delete secrets postgres-secret
sudo kubectl delete services db
sudo kubectl delete deployment db