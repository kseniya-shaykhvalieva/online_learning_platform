from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework.viewsets import ViewSet

from users.forms import UserRegisterForm
from users.models import CustomUser, Payment
from users.serializers import PaymentSerializer


class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")
    template_name = "users/user_form.html"


class PaymentViewSet(ViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
