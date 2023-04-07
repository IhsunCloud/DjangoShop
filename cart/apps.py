from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CartConfig(AppConfig):
    name = 'cart'
    verbose_name = _('Cart')
    verbose_name_plural = _('Cart')
