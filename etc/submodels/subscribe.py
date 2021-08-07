from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscribe(models.Model):
	""" Model definition for Subscription. """

	email = models.EmailField(_('Email'), null=True)

	def __str__(self):
		""" Unicode representation of Subscription. """
		return self.email

	class Meta:
		""" Meta definition for Subscription. """
		verbose_name = _('Subscription')
		verbose_name_plural = _('Subscription')