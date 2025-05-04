# Usar una imagen base oficial de Python
FROM python:3.10

# Establecer un directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto (desde el directorio actual a la carpeta /app dentro del contenedor)
COPY . /app

# Instalar las dependencias necesarias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 8000 (puerto por defecto de Django)
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]