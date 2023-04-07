from django.db import models
from django.utils.translation import gettext_lazy as _

from shop.managers import CommentManager


class Comment(models.Model):
	""" Model definition for Comments. """

	fullname = models.CharField(_('Fullname'), max_length=50, null=True)
	text = models.TextField(_('Comment Text'), max_length=256, null=True)
	rating = models.IntegerField(_('Rating'), default=0, null=True)		

	active = models.BooleanField(_('Comment Activity'), default=False, null=True)
	
	created_at = models.DateTimeField(_('Created At'), auto_now_add=True, null=True)

	class Meta:
		""" Meta definition for Comment. """
		ordering = ['-created_at']
		verbose_name = _('Comment')
		verbose_name_plural = _('Comments')

	def __str__(self):
		""" Unicode representation of Comments. """
		return 'Comment {} by {}'.format(self.comment_text, self.fullname)

	objects = CommentManager()