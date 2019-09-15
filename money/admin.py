from django.contrib import admin

from money.models import MoneyIn, MoneyOut

admin.site.register(MoneyIn)
admin.site.register(MoneyOut)
