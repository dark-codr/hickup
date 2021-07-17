from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TopicsConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'hickup.topics'
    verbose_name = _("Topic")

    def ready(self):
        try:
            import hickup.topics.signals  # noqa F401
        except ImportError:
            pass
