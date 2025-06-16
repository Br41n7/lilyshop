from django.contrib import admin
# shop/admin.py or settings/admin.py
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('brand','logo', 'banner')
    fieldsets = (
        (None, {
            'fields': ('brand', 'banner', 'about_us', 'phone', 'email','logo')
        }),

    )

    # Restrict to only one instance
    def has_add_permission(self, request):
        count = SiteSettings.objects.all().count()
        if count == 0:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False # Prevent deletion of the single instance

    # Ensure change permission is always true if an instance exists
    def has_change_permission(self, request, obj=None):
         return SiteSettings.objects.exists() # Allow change if an instance exists

