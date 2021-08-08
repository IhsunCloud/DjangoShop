from django.views import generic

from django_ajax.mixin import AJAXMixin

from shop.models import Product

class ProductListView(generic.ListView, AJAXMixin):
    template_name = 'pages/shop/shop.html'
    model = Product
    paginate_by = 12


class ProductDetailView(generic.DetailView, AJAXMixin):
    template_name = 'pages/shop/single-product.html'
    model = Product


class WishlistView(generic.ListView, AJAXMixin):
    template_name = 'pages/shop/wishlist.html'
    model = Product


class CompareListView(generic.ListView, AJAXMixin):
    template_name = 'pages/shop/compare.html'
    model = Product


class TrackOrderView(generic.TemplateView, AJAXMixin):
    template_name = 'pages/shop/track-order.html'
    model = Product


class StoreView(generic.TemplateView, AJAXMixin):
    template_name = 'pages/shop/store.html'


class BestDealsListView(generic.ListView, AJAXMixin):
    template_name = 'pages/shop/best-deals.html'
    model = Product