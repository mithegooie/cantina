from django.contrib import admin
from main.models import MarketingItem

# Register your models here.
class MarketingItemAdmin(admin.ModelAdmin):
    class Meta:
        model = MarketingItem


admin.site.register(MarketingItem, MarketingItemAdmin)