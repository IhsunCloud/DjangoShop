from .base import INSTALLED_APPS
from .base import BASE_DIR
import os


# Third-Party Apps -->
INSTALLED_APPS.append('ckeditor'),
INSTALLED_APPS.append('colorfield'),
INSTALLED_APPS.append('django_ajax'),
INSTALLED_APPS.append('mptt'),
INSTALLED_APPS.append('sorl.thumbnail'),
INSTALLED_APPS.append('taggit'),


# My Apps -->
INSTALLED_APPS.append('accounts.apps.AccountsConfig'),
INSTALLED_APPS.append('blog.apps.BlogConfig'),
INSTALLED_APPS.append('cart.apps.CartConfig'),
INSTALLED_APPS.append('etc.apps.ETCConfig'),
INSTALLED_APPS.append('painless'),
INSTALLED_APPS.append('payment.apps.PaymentConfig'),
INSTALLED_APPS.append('shop.apps.ShopConfig'),


AUTH_USER_MODEL = "accounts.User"


ALLOW_UNICODE_SLUGS = True


# CKEDITOR Configs -->
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"