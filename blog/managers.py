from django.db import models


# Category Manager
class CategoryManager(models.Manager):
	
	def active(self):
		return self.filter(status=True)


# Comment Manager
class CommentManager(models.Manager):
	
	def active(self):
		return self.filter(active=True)


# Post Manager -->
class PostManager(models.Manager):
	
	def published(self):
		return self.filter(status='P')