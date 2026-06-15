from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserCreateView, PaymentViewSet

app_name = UsersConfig.name


router = DefaultRouter()
router.register(r"payment", PaymentViewSet, basename="payment")

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
]

urlpatterns += router.urls
