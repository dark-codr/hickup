from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FeedsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hickup.feeds'
    verbose_name = _("Feeds")

    def ready(self):
        try:
            import hickup.feeds.signals  # noqa F401
        except ImportError:
            pass
