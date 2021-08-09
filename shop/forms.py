from django import forms

from shop.models import Product


# Showing Items Number
SHOWING_ITEMS_NUMBER_CHOICES = (
    ('1', '8'),
    ('2', '12'),
    ('3', '16'),
    ('4', '20'),
    ('5', '24'),
)

# Sort by
ORDER_BY = (
    ('1', 'Trending Items'),
    ('2', 'Best Sellers'),
    ('3', 'Best Rated'),
    ('4', 'Newest Items'),
    ('5', 'Price: low to high'),
    ('5', 'Price: high to low'),
)

class OrderingForm(forms.ModelForm):
    showing_items_number_field = forms.ChoiceField(choices = SHOWING_ITEMS_NUMBER_CHOICES)
    order_by_field = forms.ChoiceField(choices = ORDER_BY)

    class Meta:
        model = Product
        fields = ('__all__')