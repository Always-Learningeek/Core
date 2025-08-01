from django.core.serializers import serialize
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404


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

class PostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


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

#CBV-Base
class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, pk):
        """ Retrieve the post data """
        post = get_object_or_404(Post, pk=pk, status=True)
        serializer = self.serializer_class(post)
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