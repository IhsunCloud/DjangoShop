from django.db import models
from django.utils.translation import ugettext_lazy as _

from blog.managers import CommentManager
from blog.submodels.post import Post


class Comment(models.Model):
	""" Model definition for Comments. """

	first_name = models.CharField(_('First Name'), max_length=50, null=True)
	last_name = models.CharField(_('Last Name'), max_length=50, null=True)
	
	phone_number = models.CharField(_('Phone Number'), max_length=50, null=True)
	email = models.EmailField(null=True)
	
	message = models.TextField(_('Message'), max_length=256, null=True)
	active = models.BooleanField(_('Comment Activity'), default=False, null=True)

	post = models.ForeignKey(Post, verbose_name=_('Post'),
		related_name=_('comments'),on_delete=models.CASCADE, blank=True, null=True)
	
	created_at = models.DateTimeField(_('Created At'), auto_now_add=True, null=True)

	class Meta:
		""" Meta definition for Comment. """
		ordering = ['-created_at']
		verbose_name = _('Comment')
		verbose_name_plural = _('Comments')

	def __str__(self):
		""" Unicode representation of Comments. """
		return 'Comment {} by {} - {}'.format(self.message, self.first_name, self.last_name)

	objects = CommentManager()