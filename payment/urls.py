from django.urls import path

from .views import * 


urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
]