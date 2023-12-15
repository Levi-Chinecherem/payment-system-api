# payment/models.py
from django.db import models

class USDT_TRC20(models.Model):
    coin_name = models.CharField(max_length=255)
    qr_code = models.ImageField(upload_to='usdt_trc20_qrcodes/')
    wallet_address = models.CharField(max_length=255)
    network = models.CharField(max_length=50)

    def __str__(self):
        return self.coin_name

    class Meta:
        verbose_name = "USDT TRC20"
        verbose_name_plural = "USDT TRC20"

class USDT_ERC20(models.Model):
    coin_name = models.CharField(max_length=255)
    qr_code = models.ImageField(upload_to='usdt_erc20_qrcodes/')
    wallet_address = models.CharField(max_length=255)
    network = models.CharField(max_length=50)

    def __str__(self):
        return self.coin_name

    class Meta:
        verbose_name = "USDT ERC20"
        verbose_name_plural = "USDT ERC20"

class BTC(models.Model):
    coin_name = models.CharField(max_length=255)
    qr_code = models.ImageField(upload_to='btc_qrcodes/')
    wallet_address = models.CharField(max_length=255)
    network = models.CharField(max_length=50)

    def __str__(self):
        return self.coin_name

    class Meta:
        verbose_name = "BTC"
        verbose_name_plural = "BTC"
