from django.views import generic
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from shop.models import Product
from mysite.models import Contact
from mysite.forms import ContactForm, SubscribeForm


class IndexView(FormMixin, generic.ListView):
	template_name = 'pages/site/index.html'
	model = Product
	form_class = SubscribeForm
	title = 'index'


class AboutUsView(generic.TemplateView):
	template_name = 'pages/site/about-us.html'


class ContactUsView(SuccessMessageMixin, generic.CreateView):
	template_name = 'pages/site/contact.html'
	model = Contact
	form_class = ContactForm
	success_url = reverse_lazy('site:contact')
	success_message = 'Your Message is sent!'


class FeaturesView(generic.TemplateView):
	template_name = 'pages/site/feature.html'


class QuestionsView(generic.TemplateView):
	template_name = 'pages/site/faq.html'


class TermsConditionsView(generic.TemplateView):
	template_name = 'pages/site/terms-conditions.html'