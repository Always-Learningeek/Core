from django.core.serializers import serialize
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, IsAuthenticated
)
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from django.shortcuts import get_object_or_404
from blog.api.v1.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'author', 'status']
    search_fields = ['title', 'content']
    ordering_fields = ['published_date']

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()






'''
class PostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True,):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)




#CBV-Base
class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, pk):
        """ Retrieve the post data """
        post = get_object_or_404(Post, pk=pk, status=True)
        serializer = self.serializer_class(post, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        """ Update the post data """
        post = get_object_or_404(Post, pk=pk, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        """ Delete the post data """
        post = get_object_or_404(Post, pk=pk, status=True)
        post.delete()
        context = {
            "detail" : "Post deleted successfully"
        }
        return Response(context, status=status.HTTP_204_NO_CONTENT)
'''


'''
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def api_v1_post_list(request):
    if request.method == "GET" :
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
'''

'''
@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def api_v1_post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, status=True)
    if request.method == "GET" :
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT" :
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE" :
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''