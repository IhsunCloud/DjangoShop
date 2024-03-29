from .base import *
from .secure import *
from .packages import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
