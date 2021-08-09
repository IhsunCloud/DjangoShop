from dal import autocomplete

from django import forms

from shop.models import Product


# Search Options
CATEGORY_CHOICES =(
    ('1', 'All Categories'),
    ('2', 'Computer'),
    ('3', 'Laptop'),
    ('4', 'Mobile'),
    ('5', 'Gadget'),
)

class SearchForm(forms.ModelForm):
    category_field = forms.ChoiceField(choices = CATEGORY_CHOICES)

    class Meta:
        model = Product
        fields = ('title', 'category_field',)
        widgets = {
            'title': autocomplete.ModelSelect2(url='product-autocomplete')
        }
