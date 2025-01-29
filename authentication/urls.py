from authentication.views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView

app_name = 'authentication'
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token-refresh'),
]