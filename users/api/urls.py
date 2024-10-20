from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api-token-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
    path('api-token-verify/', TokenVerifyView.as_view(), name='token_verify'),  # Verify token
]