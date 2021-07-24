from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
	""" Model definition for Contacts. """

	first_name = models.CharField(_('First Name'), max_length=50, null=True)
	last_name = models.CharField(_('Last Name'), max_length=50, null=True)
	
	phone_number = models.CharField(_('Phone Number'), max_length=50, null=True)
	email = models.EmailField(null=True)
	
	message = models.TextField(_('Message'), max_length=256, null=True)
	
	created_at = models.DateTimeField(_('Created At'), auto_now_add=True, null=True)

	class Meta:
		""" Meta definition for Contact. """
		ordering = ['-created_at']
		verbose_name = _('Contact'),
		verbose_name_plural = _('Contact'),

	def __str__(self):
		""" Unicode representation of Contacts. """
		return 'Message {} by {} - {}'.format(self.message, self.first_name, self.last_name)