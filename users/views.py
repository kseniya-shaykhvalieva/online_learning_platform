from django.urls import reverse_lazy
from django.views.generic import CreateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from users.forms import UserRegisterForm
from users.models import CustomUser, Payment
from users.serializers import PaymentSerializer


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
