from django.contrib import admin
from main.models import MarketingItem, Announcement

# Register your models here.
class MarketingItemAdmin(admin.ModelAdmin):
    class Meta:
        model = MarketingItem

admin.site.register(MarketingItem, MarketingItemAdmin)

class AnnouncementAdmin(admin.ModelAdmin):
    class Meta:
        model = Announcement

admin.site.register(Announcement, AnnouncementAdmin)
