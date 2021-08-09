from django.db.models import Q
from django.shortcuts import render
from django.views import generic

from dal import autocomplete

from shop.models import Product


class ProductAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Product.objects.all()

        if self.q:
            qs = qs.filter(title__contains=self.q)
        return qs


class SearchResultsView(generic.ListView):
    model = Product
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list