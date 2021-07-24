from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField

from .category import Category
from .comment import Comment

from mptt.models import TreeForeignKey
from taggit.managers import TaggableManager
from shop.managers import ProductManager

from painless.upload_to import product_directory_path


class Product(models.Model):
	""" Model definition for Products. """

	AVAILABILITY_STATUS = (
		('A', 'Available'),
		('N', 'Not Available'),
		('S', 'Soon'),
	)

	STATUS_CHOICES = (
		('D', 'DRAFT'),
		('P', 'PUBLISHED'),
	)

	title = models.CharField(_('Title'), max_length=128, null=True)
	slug = models.SlugField(_('Slug'), unique=True)
	description = RichTextUploadingField(_('Description'), null=True)

	price = models.DecimalField(_("Price"), max_digits=10, decimal_places=0, null=True, blank=True)
	call_for_get_price = models.BooleanField(_('Call For Get Price'), default=False, null=True, blank=True)
	discount = models.DecimalField(_('Discount'), max_digits=10, decimal_places=0, null=True, blank=True)

	color = models.CharField(_('Color'), max_length=64)
	status = models.CharField(_('Status'),
		max_length=1, choices=STATUS_CHOICES , null=True)

	availability = models.CharField(_('Availability'),
		max_length=1, default='A', choices=AVAILABILITY_STATUS, null=True)
	
	category = TreeForeignKey(Category,
		verbose_name=_('Category'), related_name='products', on_delete = models.CASCADE, null=True)
	
	comment = models.ForeignKey(Comment,verbose_name=_('Comment'),
		related_name='products', on_delete=models.CASCADE, null=True, blank=True)

	tags = TaggableManager()

	created_at = models.DateTimeField(_('Product Created At'), auto_now_add=True)
	modified_at = models.DateTimeField(_("Product Modified At"), auto_now=True)

	class Meta:
		""" Meta definition for Products. """
		verbose_name = _('Products')
		verbose_name_plural = _('Products')
		index_together = (('id', 'slug'))
		ordering = ('-created_at',)

	def __str__(self):
		""" Unicode representation of Products. """
		return self.title

	def get_final_price(self):
		""" Calculate the final price of the discounted product. """
		return self.price - (self.price * discount / 100)

	def has_discount(self):
		if self.discount:
			return True
		return False

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title, allow_unicode=True)
		super(Product, self).save(*args, **kwargs)

	managers = ProductManager()