from django.urls import path

from .views import *

app_name = 'search'


urlpatterns = [
    path('', ),
    path('product-autocomplete', ProductAutocomplete.as_view(), name = 'product-autocomplete'),
]