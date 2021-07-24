from django.views import generic

from shop.models import Product


class ProductListView(generic.ListView):
    template_name = 'pages/shop/shop.html'
    model = Product
    paginate_by = 12


class ProductDetailView(generic.DetailView):
    template_name = 'pages/shop/single-product.html'
    model = Product


class WishlistView(generic.ListView):
    template_name = 'pages/shop/wishlist.html'
    model = Product


class CompareListView(generic.ListView):
    template_name = 'pages/shop/compare.html'
    model = Product


class TrackOrderView(generic.TemplateView):
    template_name = 'pages/shop/track-order.html'
    model = Product


class StoreView(generic.TemplateView):
    template_name = 'pages/shop/store.html'