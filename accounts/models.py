from django.db import models
from django.contrib.auth.models import  AbstractUser


class User(AbstractUser):
	""" My Customized User Model. """
	
	username = models.CharField(max_length=64,unique=True, null=True, blank=True)
	avatar = models.ImageField(upload_to='profiles/', null=True, blank=True)
	phone = models.CharField(max_length=16, unique=True)
	