from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MysiteConfig(AppConfig):
    name = 'mysite'
    verbose_name = _('Site')
    verbose_name_plural = _('Site')