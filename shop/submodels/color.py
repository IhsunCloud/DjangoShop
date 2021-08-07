from django.db import models
from django.utils.translation import ugettext_lazy as _

from colorfield.fields import ColorField

# from .product import Product


class Color(models.Model):
	""" Model definition for Colors. """

	title = models.CharField(_('Title'), max_length=50)
	color = ColorField(_('Color'), default='#FF0000')
	# product = models.ForeignKey(
	# 	Product, 
	# 	verbose_name=_('Product'),
	# 	related_name='color',
	# 	on_delete = models.CASCADE,
	# 	null=True
	# )
	
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('Color')
		verbose_name_plural = _('Colors')