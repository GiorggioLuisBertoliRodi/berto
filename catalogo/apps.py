from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate

class CatalogoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalogo'

    def ready(self):
        # Crear superusuario automáticamente en Render
        def create_admin(sender, **kwargs):
            if getattr(settings, "RENDER", False):  # Solo en Render
                User = get_user_model()
                if not User.objects.filter(username="admin").exists():
                    User.objects.create_superuser(
                        username="admin",
                        email="",       # puedes poner un email si quieres
                        password="admin1234"
                    )

        post_migrate.connect(create_admin, sender=self)
