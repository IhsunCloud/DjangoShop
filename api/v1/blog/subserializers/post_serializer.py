from rest_framework import serializers

from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post model.
    """
    author = serializers.ReadOnlyField(source="post.author")
    author_id = serializers.ReadOnlyField(source="post.id")
    
    class Meta:
        model = Post
        fields = '__all__'