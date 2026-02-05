from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate

class CatalogoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalogo'
