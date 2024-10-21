from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path(
        "api-token-auth/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # Token authentication
    path(
        "api-token-refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # Refresh token
    path(
        "api-token-verify/", TokenVerifyView.as_view(), name="token_verify"
    ),  # Verify token
    path("api/register/", views.register_user, name="register_user"),
    path("api/login/", views.login_user, name="login_user"),
    path("api/logout/", views.logout_user, name="logout_user"),
]
