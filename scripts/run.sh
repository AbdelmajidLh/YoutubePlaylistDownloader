#!/bin/bash

# Création venv
python3 -m venv .venv
source .venv/bin/activate

# Installation du projet
pip install --upgrade pip
pip install .

# Lancement de l'application
python -m main
