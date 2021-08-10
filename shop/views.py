from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.db.models import Q
from django.views import generic

from shop.models import Product


class ProductListView(generic.ListView):
	template_name = 'pages/shop/shop.html'
	model = Product
	paginate_by = 12

	# def get_queryset(self):
	# 	object_list = Product.objects.published().order_by('-created_at')

	# 	title = self.request.GET.get('title', None)

	# 	if title:
	# 		object_list = object_list.filter(title__icontains = title)

	# 	query = self.request.GET.get('q')
	# 	object_list = Product.objects.filter(
	# 		Q(title__icontains=query)
	# 	)
	# 	return object_list
	
	# def get_context_data(self, **kwargs):
	# 	context = super(ProductListView, self).get_context_data(**kwargs) 
	# 	list_product = Product.objects.all()
	# 	paginator = Paginator(list_product, self.paginate_by)

	# 	page = self.request.GET.get('page')

	# 	try:
	# 		file_product = paginator.page(page)
	# 	except PageNotAnInteger:
	# 		file_product = paginator.page(1)
	# 	except EmptyPage:
	# 		file_product = paginator.page(paginator.num_pages)

	# 	context['list_product'] = file_product
	# 	return context


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


class BestDealsListView(generic.ListView):
	template_name = 'pages/shop/best-deals.html'
	model = Product