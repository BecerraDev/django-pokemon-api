# Usar una imagen base oficial de Python 
FROM python:3.10

# Establecer un directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Copiar el script de creación de .env al contenedor
COPY create_env.sh /app/create_env.sh

# Darle permisos de ejecución al script
RUN chmod +x /app/create_env.sh

# Ejecutar el script para crear el .env
RUN /app/create_env.sh

# Instalar las dependencias necesarias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Ejecutar migraciones y crear superusuario automáticamente
RUN python manage.py migrate && python create_superuser.py

# Exponer el puerto 8000 (puerto por defecto de Django)
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]