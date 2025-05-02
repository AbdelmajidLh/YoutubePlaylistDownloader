@echo off

REM Créer et activer l'environnement virtuel
python -m venv .venv
call .venv\Scripts\activate

REM Mettre à jour pip
python -m pip install --upgrade pip

REM Installer le projet localement
pip install .

REM Lancer l'application
python -m main
