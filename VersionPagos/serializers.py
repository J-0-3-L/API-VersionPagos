from rest_framework import serializers
from .models import Service, PaymentUser, ExpiredPayments

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'description', 'logo')

class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentUser
        fields = ('id', 'user_id', 'service_id', 'amount', 'payment_date', 'expiration_date')

class ExpiredPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpiredPayments
        fields = ('id', 'pay_user_id', 'penalty_fee_amount')
