from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MLConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    verbose_name = _("Machine Learning")

    def ready(self):
        from utils.ml.helpers import MLHelperUtils
        MLHelperUtils.Model.load()
