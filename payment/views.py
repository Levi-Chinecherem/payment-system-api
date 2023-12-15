# payment/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import USDT_TRC20, USDT_ERC20, BTC
from .serializers import USDT_TRC20Serializer, USDT_ERC20Serializer, BTCSerializer

class LatestUSDT_TRC20(APIView):
    def get(self, request, *args, **kwargs):
        usdt_trc20 = USDT_TRC20.objects.all().order_by('-id').first()
        serializer = USDT_TRC20Serializer(usdt_trc20)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LatestUSDT_ERC20(APIView):
    def get(self, request, *args, **kwargs):
        usdt_erc20 = USDT_ERC20.objects.all().order_by('-id').first()
        serializer = USDT_ERC20Serializer(usdt_erc20)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LatestBTC(APIView):
    def get(self, request, *args, **kwargs):
        btc = BTC.objects.all().order_by('-id').first()
        serializer = BTCSerializer(btc)
        return Response(serializer.data, status=status.HTTP_200_OK)
