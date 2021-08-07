from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ETCConfig(AppConfig):
    name = 'etc'
    verbose_name = _('ETC')
    verbose_name_plural = _('ETC')