from django.urls import path
from . import views


app_name = 'api-v1'

urlpatterns = [
    path('post/', views.api_v1_post_list, name='api-post-list'),
    path('post-detail/<int:pk>/' , views.api_v1_post_detail , name='api-post-detail'),
]