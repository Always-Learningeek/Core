from django.urls import path, include
from . import views
#from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'api-v1'

urlpatterns = [
    path('registration/', views.RegistrationAPIView.as_view(), name='registration'),
    path('change_password/', views.ChangePasswordAPIView.as_view(), name='login'),
    path('token/login/', views.CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name='token-logout'),
    # JWT login
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='jwt-verify'),

]
