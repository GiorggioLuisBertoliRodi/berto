import os
import django

# Inicializa Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.core.management import call_command

# Carga el fixture
call_command("loaddata", "superuser.json")
print("Superusuario cargado correctamente.")
