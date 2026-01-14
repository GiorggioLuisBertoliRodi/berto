#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    # en alguna app, por ejemplo en catalogo/apps.py

from django.apps import AppConfig
from django.db.models.signals import post_migrate

class CatalogoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalogo'

    def ready(self):
        from django.contrib.auth import get_user_model
        from django.conf import settings
        from django.db.models.signals import post_migrate

        def create_superuser(sender, **kwargs):
            if settings.RENDER:  # si quieres que solo sea en Render
                User = get_user_model()
                if not User.objects.filter(username="admin").exists():
                    User.objects.create_superuser(
                        username="admin",
                        email="",
                        password="admin1234"
                    )

        post_migrate.connect(create_superuser, sender=self)

