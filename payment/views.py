from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


class CheckoutView(generic.TemplateView):
    template_name = 'pages/shop/checkout.html'