from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


app_name = 'api-v1'

router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")
urlpatterns = router.urls

'''
urlpatterns = [
    #path('post/', views.api_v1_post_list, name='api-post-list'),
    #path('post/', views.PostList.as_view(), name='api-post-list'),
    #path('post/<int:pk>/' , views.api_v1_post_detail , name='api-post-detail'),
    #path('post/<int:pk>/', views.PostDetail.as_view(), name='api-post-detail'),
     #path('post/',views.PostViewSet.as_view({'get':'list','post':'create'}),name='post-list'),
     #path('post/<int:pk>/',views.PostViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name="post-detail"),
]
'''