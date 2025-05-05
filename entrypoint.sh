#!/bin/sh

# Migraciones
python manage.py migrate --noinput

# Crear superusuario si no existe
python create_superuser.py

# Ejecutar servidor
python manage.py runserver 0.0.0.0:8000