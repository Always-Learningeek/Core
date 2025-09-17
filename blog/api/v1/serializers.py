from rest_framework import serializers
from unicodedata import category

from blog.models import Post, Category

''' 
class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    

    def create(self, validated_data):
        return Post.objects.create()
'''
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','name']


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['id','author','title','content','snippet', 'category', 'status', 'relative_url', 'created_date','published_date']

