from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.models import User


class SignupForm(UserCreationForm):
	image = forms.ImageField(required=False)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'image')


class LoginForm(AuthenticationForm):
	username = forms.CharField(label='Email / Username')
	remember_me = forms.BooleanField(required=False)