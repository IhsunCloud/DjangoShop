from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from django_ajax.mixin import AJAXMixin

from blog.models import Category, Comment, Post
from blog.forms import CommentForm


class PostsView(AJAXMixin, generic.ListView):
	model = Post
	template_name = 'pages/blog/posts.html'
	paginate_by = 1

	def get_context_data(self, **kwargs):
		context = super(PostsView, self).get_context_data(**kwargs)
		context['recent_posts'] = Post.objects.all()[:3]
		return context
		

class SinglePostView(FormMixin, generic.DetailView, AJAXMixin):
	model = Post
	template_name = 'pages/blog/single-post.html'

	def get_success_url(self):
		return reverse('weblog:single-post', kwargs={'slug': self.object.slug})

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = CommentForm(request.POST or None)
		
		if form.is_valid():
			form.instance.posts = Post.objects.get(pk=self.object.pk)
			form.save()
			return self.form_valid(form)
		
		else:
			return self.form_invalid(form)

	def get_context_data(self, **kwargs):
		context = super(SinglePostView, self).get_context_data(**kwargs)
		context['recent_posts'] = Post.objects.all()[:3]
		return context