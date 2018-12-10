from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "shippers_owned_container_tracker.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
