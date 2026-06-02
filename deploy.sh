#!/bin/bash

echo "Iniciando el despliegue automatico"

cd /home/juanpablomozuca/moto-api

echo "Trayendo la ultima version desde git"

git pull origin master

echo "Asegurando las dependencias"
source venv/bin/activate
pip install -r requirements.txt --quiet


echo "Reiniciando gunicorn"
sudo systemctl restart moto-api.service


echo "Despliegue completado. Estado Actual:"
sudo systemctl status moto-api.service | grep "Active:" 
