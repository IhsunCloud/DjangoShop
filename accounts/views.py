from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from accounts.forms import SignupForm, LoginForm


class Register(generic.CreateView):
	form_class = SignupForm
	template_name = "pages/registration/register.html"
	success_url = reverse_lazy('site:index')

	def form_valid(self, form):
		user = form.save(commit=False)
		user.is_active = True
		user.save()

		username = form.cleaned_data.get('username')
		raw_password = form.cleaned_data.get('password1')

		user = authenticate(username = username, password = raw_password)
		login(self.request, user)
		
		return redirect(self.success_url)


class Login(LoginView):
	template_name = 'pages/registration/login.html'
	form_class = LoginForm
	success_url = reverse_lazy('site:index')

	def form_valid(self, form):
		remember_me = form.cleaned_data['remember_me']

		if not remember_me:
			self.request.session.set_expiry(0)
			self.request.session.modified = True

		return super(Login, self).form_valid(form)