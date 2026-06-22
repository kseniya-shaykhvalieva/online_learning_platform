from django.urls import reverse_lazy
from django.views.generic import CreateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from users.forms import UserRegisterForm
from users.models import CustomUser, Payment
from users.permissions import IsOwner
from users.serializers import PaymentSerializer, UserSerializer


class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")
    template_name = "users/user_form.html"


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ("pay_date",)
    filterset_fields = ("course", "lesson", "pay_method",)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            self.permission_classes = (IsOwner,)
        elif self.action in ["update", "destroy"]:
            self.permission_classes = (IsAdminUser,)
        return super().get_permissions()


class UserCreateAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsOwner,)


class UserDestroyAPIView(DestroyAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated, IsOwner,)
