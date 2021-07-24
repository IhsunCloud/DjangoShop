from django.urls import path

from . import views

app_name = 'cart'


urlpatterns = [
    path('', views.CartDetailView.as_view(), name = 'cart-detail'),
    path('add/<int:pk>/', views.CartAddView.as_view(), name = 'cart-add'),
    path('remove/<int:pk>/', views.CartRemoveView.as_view(), name = 'cart-remove'),
]