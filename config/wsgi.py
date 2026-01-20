import sys
import os

# Ruta de tu proyecto
project_home = '/home/tu_usuario/berto'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Nombre de tu proyecto Django (la carpeta con settings.py)
os.environ['DJANGO_SETTINGS_MODULE'] = 'berto.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
