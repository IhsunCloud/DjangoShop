from django.db.models.signals import post_save
from django.dispatch import receiver

from cart.models import OrderItem

import math


@receiver(post_save, sender=OrderItem)
def cart_update_price(sender, instance, **kwargs):

    if instance.products.has_discount:
        # total = math.fsum(instance.price * instance.quantity for instance in instance.products.all)    
        instance.price = instance.price - (instance.price * instance.products.discount / 100)
        instance.save()
