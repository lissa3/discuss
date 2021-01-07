from django.apps import AppConfig


class IdeasConfig(AppConfig):
    name = 'ideas'
    def ready(self):
        # print("greet form app.py")
        from ideas import signals
