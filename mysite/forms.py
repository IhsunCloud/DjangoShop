from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from mysite.models import Contact, Subscribe


class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = '__all__'

	def clean_fullname(self):
		first_name = self.cleaned_data.get('first_name')

		except_values = ['<', '>', '/']

		for e_v in except_values:

			if e_v in first_name:

				raise ValidationError(
					_('You can not use `<, >, /`'),
					code = _('forbidden')
				)

		return first_name

	def clean_last_name(self):
		last_name = self.cleaned_data.get('last_name')

		except_values = ['<', '>', '/']

		for e_v in except_values:

			if e_v in last_name:

				raise ValidationError(
					_('You can not use `<, >, /`'),
					code = _('forbidden')
				)

		return last_name

	def clean_phone_number(self):
		phone_number = self.cleaned_data.get('phone_number')

		except_values = ['<', '>', '/']

		for e_v in except_values:

			if e_v in phone_number:

				raise ValidationError(
					_('You can not use `<, >, /`'),
					code = _('forbidden')
				)

		return phone_number

	def clean_message(self):
		phone_number = self.cleaned_data.get('message')

		except_values = ['<', '>', '/']

		for e_v in except_values:

			if e_v in message:

				raise ValidationError(
					_('You can not use `<, >, /`'),
					code = _('forbidden')
				)

		return message

	def clean(self):
		cleaned_data = super(ContactForm, self).clean()

		first_name = cleaned_data.get('first_name')
		last_name = cleaned_data.get('last_name')
		phone_number = cleaned_data.get('phone_number')
		email = cleaned_data.get('email')
		message = cleaned_data.get('message')

		if not fullname:
			raise ValidationError(
				_('Please fill this field'),
				code = _('forbidden')
			)

		if not last_name:
			raise ValidationError(
				_('Please fill this field'),
				code = _('forbidden')
			)

		if not email:
			raise ValidationError(
				_('Please fill this field'),
				code = _('forbidden')
			)

		if not message:
			raise ValidationError(
				_('Please fill this field'),
				code = _('forbidden')
			)


class SubscribeForm(forms.ModelForm):

	class Meta:
		model = Subscribe
		fields = '__all__'