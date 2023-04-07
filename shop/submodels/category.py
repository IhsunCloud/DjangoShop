from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.models import TreeForeignKey, MPTTModel
from shop.managers import CategoryManager


class Category(MPTTModel):
	""" Model definition for Categories. """

	name = models.CharField(_('Name'), max_length=50, unique=True)
	slug = models.SlugField(_('Slug'), null=True, allow_unicode=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, 
		null=True, blank=True, related_name='children')
	status = models.BooleanField(default=True)

	class MPTTMeta:
		order_insertion_by = ['name']
	
	class Meta:
		""" Meta definition of Categories. """
		unique_together = (('parent', 'slug',))
		verbose_name = _('Category')
		verbose_name_plural = _('Categories')

	def __repr__(self):
		""" Unicode representation of Categories. """
		return self.name

	def __str__(self):
		""" Unicode representation of Categories. """
		return self.name

	objects = CategoryManager()