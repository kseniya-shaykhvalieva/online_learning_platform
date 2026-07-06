from rest_framework.serializers import ModelSerializer

from users.models import Payment, CustomUser


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
