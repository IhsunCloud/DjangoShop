from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver

from kernel.settings.secure import EMAIL_HOST_USER

from accounts.models import Email
from shop.models import Product


@receiver(post_save, sender=Product)
def SendEmail(sender , instance, created, **kwargs):
    """ Send email to users when create a product with discount. """
    
    if created:
        
        if instance.has_discount:
            emails = list(Email.objects.values('email'))
            
            recepients = []
            for i in range(0, len(emails)):
                recepients.append(emails[i]['email'])
            
            send_mail('Do not miss our discounted product!', str(instance.title), EMAIL_HOST_USER, recepients, fail_silently=False)
        
        else:
            pass
