from django import models
from django.utils.translation import ugettext as _


class Timestamped(models.Model):
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    modified_at = models.DateTimeField(_('Modified At'), auto_now=True)