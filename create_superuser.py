# create_superuser.py
import os
import django
from dotenv import load_dotenv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "login_python_api.settings")
load_dotenv()
django.setup()

from django.contrib.auth.models import User

username = os.getenv("DJANGO_SUPERUSER_USERNAME")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

if username and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, password)
        print(f"✅ Superusuario '{username}' creado.")
    else:
        print(f"ℹ️ El usuario '{username}' ya existe.")
else:
    print("⚠️ Faltan variables de entorno.")