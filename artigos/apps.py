from django.apps import AppConfig


class ArtigosConfig(AppConfig):
    name = 'artigos'

    def ready(self):
        import artigos.signals  # noqa
