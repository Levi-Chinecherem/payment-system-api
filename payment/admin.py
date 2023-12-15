# payment/admin.py
from django.contrib import admin
from .models import USDT_TRC20, USDT_ERC20, BTC

class USDT_TRC20Admin(admin.ModelAdmin):
    list_display = ('coin_name', 'wallet_address', 'network')
    search_fields = ('coin_name', 'wallet_address', 'network')
    list_filter = ('network',)

class USDT_ERC20Admin(admin.ModelAdmin):
    list_display = ('coin_name', 'wallet_address', 'network')
    search_fields = ('coin_name', 'wallet_address', 'network')
    list_filter = ('network',)

class BTCAdmin(admin.ModelAdmin):
    list_display = ('coin_name', 'wallet_address', 'network')
    search_fields = ('coin_name', 'wallet_address', 'network')
    list_filter = ('network',)

admin.site.site_header = "BI_PAY Admin"
admin.site.site_title = "Payment System Admin"
admin.site.index_title = "Welcome to the Payment System (BI_PAY) Admin Panel"

admin.site.register(USDT_TRC20, USDT_TRC20Admin)
admin.site.register(USDT_ERC20, USDT_ERC20Admin)
admin.site.register(BTC, BTCAdmin)
