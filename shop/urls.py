from django.urls import path

from .views import *

app_name = 'shop'


urlpatterns = [
    path('', ProductListView.as_view(), name = 'product-list'),
    path('best-deals/', BestDealsListView.as_view(), name = 'best-deals'),
    path('compare/', CompareListView.as_view(), name = 'compare'),
    path('locate-store/', StoreView.as_view(), name = 'store'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name = 'single-product'),
    path('track-order/', TrackOrderView.as_view(), name ='track-order'),
    path('wishlist/', WishlistView.as_view(), name = 'wishlist'),
]