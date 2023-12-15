# payment/serializers.py
from rest_framework import serializers
from .models import USDT_TRC20, USDT_ERC20, BTC

class USDT_TRC20Serializer(serializers.ModelSerializer):
    class Meta:
        model = USDT_TRC20
        fields = '__all__'

class USDT_ERC20Serializer(serializers.ModelSerializer):
    class Meta:
        model = USDT_ERC20
        fields = '__all__'

class BTCSerializer(serializers.ModelSerializer):
    class Meta:
        model = BTC
        fields = '__all__'
