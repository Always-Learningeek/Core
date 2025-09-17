from rest_framework import serializers
from blog.models import Post, Category
from accounts.models import Profile

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
    read_only_fields = ['author']

    class Meta:
        model = Post
        fields = ['id', 'author', 'image', 'title','content','snippet', 'category', 'status', 'relative_url', 'created_date','published_date']
        read_only_fields= ['author']

    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet', None)
        else:
            rep.pop('content', None)
        rep['Category'] = CategorySerializer(instance.category, context={'request': request}).data
        return rep

    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id =self.context['request'].user.id)
        return super().create(validated_data)