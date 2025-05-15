from django.apps import AppConfig


class OffboardingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "offboarding"

    def ready(self):
        from django.urls import include, path

        from friday.friday_settings import APPS
        from friday.urls import urlpatterns

        APPS.append("offboarding")
        urlpatterns.append(
            path("offboarding/", include("offboarding.urls")),
        )
        super().ready()
