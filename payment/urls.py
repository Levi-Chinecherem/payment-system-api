# payment/urls.py
from django.urls import path
from .views import LatestUSDT_TRC20, LatestUSDT_ERC20, LatestBTC

urlpatterns = [
    path('usdt-trc20/', LatestUSDT_TRC20.as_view(), name='latest_usdt_trc20'),
    path('usdt-erc20/', LatestUSDT_ERC20.as_view(), name='latest_usdt_erc20'),
    path('btc/', LatestBTC.as_view(), name='latest_btc'),
]
