# create_superuser.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "login_python_api.settings")
django.setup()

from django.contrib.auth.models import User

# Obtener las variables de entorno
username = os.getenv("SUPERUSER_USERNAME")
password = os.getenv("SUPERUSER_PASSWORD")
email = os.getenv("SUPERUSER_EMAIL", "")  # Si no está en el .env, por defecto será una cadena vacía

# Verificar si el superusuario ya existe
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print(f"El superusuario '{username}' ya existe.")