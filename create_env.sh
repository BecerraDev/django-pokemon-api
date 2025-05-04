#!/bin/sh

# Verifica si el archivo .env ya existe
if [ ! -f .env ]; then
    echo ".env no encontrado, creando a partir de .env.example"
    cp .env.example .env
    echo "Archivo .env creado con éxito"
fi


# Verifica si hay un .env creado, sino .env toma los valores de .env.example