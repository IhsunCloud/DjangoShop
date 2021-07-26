from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = _('Weblog')
    verbose_name_plural = _('Weblog')
