from django.db import models

from django.core.validators import FileExtensionValidator

from django.utils.translation import gettext_lazy as _

from painless.upload_to import product_directory_path

from .product import Product


class Image(models.Model):
    """ Model definition for Images. """

    image = models.ImageField(_('Image'),
        upload_to='product',
        validators=[FileExtensionValidator(['jpg', 'png'])],
        null=True, blank=True
    )
    product = models.ForeignKey(Product, related_name='images', null=True, on_delete = models.CASCADE)