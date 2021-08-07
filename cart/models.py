from django.db import models
from django.utils.translation import ugettext as _

from accounts.models import User
from shop.models import Product


class Order(models.Model):
	""" Model definition for Orders. """

	customer = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		""" Unicode representation of Orders. """
		return  self.customer.fullname


class OrderItem(models.Model):
	""" Model definition for Cart Items. """

	order = models.ForeignKey(Order, verbose_name=_('Order'), related_name='items',
		on_delete=models.CASCADE, null=True)
	products = models.ForeignKey(Product, related_name='order_items', verbose_name=_('Product'),
		on_delete=models.CASCADE, null=True)

	price = models.DecimalField(_("Price"), max_digits=10, decimal_places=0, null=True)
	quantity = models.IntegerField(_('Quantity'), null=True)

	def __str__(self):
		""" Unicode representation of Order Items. """
		return self.products.title + self.price