from .models import SiteSettings

def site_settings(request):
    """
    Context processor to add site settings to the context.
    """
    try:
        settings = SiteSettings.objects.get()
    except SiteSettings.DoesNotExist:
        # Create default settings if none exist
        settings = SiteSettings.objects.create()
    return {'site_settings': settings}

