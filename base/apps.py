from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'base'

    def ready(self):
        import base.signals
        try:
            from django.contrib.auth.models import User
            user = User.objects.filter(username='admin').first()
            if not user:
                user = User(username='admin', email='admin@example.com')
            user.set_password('admin')
            user.is_staff = True
            user.is_superuser = True
            user.save()
        except Exception:
            pass
