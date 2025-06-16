from django.db import models
from colorfield.fields import ColorField
# Create your models here.

class SiteSettings(models.Model):
    # Existing fields from your template's site_info
    brand = models.CharField(max_length=100, default="My Awesome Shop")
    about_us = models.TextField(blank=True, help_text="Text for the footer about us section.")
    phone = models.CharField(max_length=20, blank=True, help_text="Contact phone number.")
    email = models.EmailField(blank=True, help_text="Contact email address.")
    logo = models.ImageField(upload_to='site_logo',null=True,blank=True,help_text='site logo ')
    banner = models.ImageField(upload_to='banner',default="img/image.jpg",help_text='banner image')

    class Meta:
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"



