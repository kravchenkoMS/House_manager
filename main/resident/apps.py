from django.apps import AppConfig


class ResidentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "resident"
    def ready(self): # коли запускається додаток resident, активуються сигнали
        import resident.signals