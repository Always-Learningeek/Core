from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('post/', views.api_post_list_view, name='api-post-list'),
]