from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'base'

    def ready(self):
        import base.signals
        try:
            from django.contrib.auth.models import User
            # Create user 'admin' with blank email so signal doesn't rename it
            user = User.objects.filter(username='admin').first()
            if not user:
                user = User(username='admin', email='')
            user.set_password('admin')
            user.email = ''
            user.is_staff = True
            user.is_superuser = True
            user.save()

            # Also ensure admin@example.com with password 'admin' exists
            user_email = User.objects.filter(username='admin@example.com').first()
            if not user_email:
                user_email = User(username='admin@example.com', email='admin@example.com')
            user_email.set_password('admin')
            user_email.is_staff = True
            user_email.is_superuser = True
            user_email.save()
        except Exception:
            pass
