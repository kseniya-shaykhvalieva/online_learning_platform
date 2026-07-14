from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    PaymentSuccessURLView,
    PaymentViewSet,
    UserCreateAPIView,
    UserCreateView,
    UserDestroyAPIView,
    UserListAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
)

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"payment", PaymentViewSet, basename="payment")

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("api_login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="api_login"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
    path("user_create/", UserCreateAPIView.as_view(), name="user_create"),
    path("users_list/", UserListAPIView.as_view(), name="users_list"),
    path("user_detail/", UserRetrieveAPIView.as_view(), name="user_detail"),
    path("user_update/", UserUpdateAPIView.as_view(), name="user_update"),
    path("user_delete/", UserDestroyAPIView.as_view(), name="user_delete"),
    path("payment_success/", PaymentSuccessURLView.as_view(), name="payment_success"),
]

urlpatterns += router.urls
