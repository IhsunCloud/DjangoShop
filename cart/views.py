from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from django.views import generic

from django_ajax.mixin import AJAXMixin

from .cart import Cart
from .forms import CartAddProductForm

from shop.models import Product


class CartAddView(AJAXMixin, generic.View):

    def post(self, request, pk, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id = pk)
        form = CartAddProductForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, product_count=cd['product_count'], update_count=cd['update'])
        
        return redirect('cart:cart_detail')


class CartRemoveView(AJAXMixin, generic.View):

    def post(self, request, product_id, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id = product_id)
        cart.remove(product)

        return redirect('cart:cart_detail')


class CartDetailView(AJAXMixin, generic.View):
    template_name = 'pages/shop/cart.html'

    def get(self, request, *args, **kwargs):
        cart = Cart(request)

        for item in cart:
            item['update_product_count_form'] = CartAddProductForm(initial={'product_count': item['product_count'], 'update': True})
        return render(request, 'pages/cart/detail.html', {'cart': cart})