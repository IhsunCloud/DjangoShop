from rest_framework import serializers

from shop.models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model.
    """
    author = serializers.ReadOnlyField(source="post.author")
    author_id = serializers.ReadOnlyField(source="post.id")
    
    class Meta:
        model = Product
        fields = '__all__'