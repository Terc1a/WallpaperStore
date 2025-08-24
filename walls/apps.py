from django.apps import AppConfig


class WallsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'walls'

    def ready(self):
        import django
        from django.conf import settings
        from django.template.engine import Engine
        # Добавляем путь к шаблонам админки
        admin_templates = 'walls/templates/admin'
        if admin_templates not in settings.TEMPLATES[0]['DIRS']:
            settings.TEMPLATES[0]['DIRS'].append(admin_templates)
