#!/bin/bash

GREEN="\e[1;32m"
RESET="\e[0m"

source ./django_venv/bin/activate
echo -e "↘️ ↘️  ${GREEN}We are in the django virtual environment${RESET}↙️ ↙️"
which python3
echo -e "\n↘️ ↘️  ${GREEN}This is the Django version${RESET}↙️ ↙️"
python3 -m django --version
cd djangoproject
python3 manage.py migrate
echo -e "✅ ${GREEN}Django Running The Server${RESET}✅"
gnome-terminal -- bash -c 'python3 manage.py runserver; exec bash'

