from django.urls import path, include
from . import views


app_name = 'blog'

urlpatterns = [
    path('post/', views.api_post_list_view, name='api-post-list'),
    path("api/v1/", include("blog.api.v1.urls")),
]