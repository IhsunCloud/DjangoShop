from django.db import models

from django.utils.html import format_html
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField

from .category import Category
from accounts.models import User
from mptt.models import TreeForeignKey, MPTTModel

from blog.managers import PostManager
from taggit.managers import TaggableManager

from painless.upload_to import post_directory_path


class Post(models.Model):
	""" Model definition for Posts. """

	STATUS_CHOICES =(
		('D', 'Draft'),
		('P', 'Published'),
	)

	title = models.CharField(_('Title'), max_length=200)
	slug = models.SlugField(_('Slug'), max_length=100, allow_unicode=True, unique=True)
	description = RichTextUploadingField(_('Description'))
	
	author = models.ForeignKey(User, related_name='author_posts', null=True, on_delete=models.CASCADE)
	category = TreeForeignKey(Category, related_name='posts', on_delete=models.CASCADE, null=True)
	status = models.CharField(_('Status'), max_length=1, choices=STATUS_CHOICES)
	
	image = models.ImageField(_('Image'), upload_to=post_directory_path, null=True)

	tags = TaggableManager()
	
	created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

	class Meta:
		verbose_name = _('Post')
		verbose_name_plural = _('Posts')
		ordering = ['-created_at']

	def __str__(self):
		return self.title

	def __repr__(self):
		return self.__str__()

	def thumbnail_tag(self):
		return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.thumbnail.url))
	thumbnail_tag.short_description = "image"

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title, allow_unicode=True)
		super(Post, self).save(*args, **kwargs)

	objects = PostManager()