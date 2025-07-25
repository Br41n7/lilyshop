# Generated by Django 5.1.4 on 2025-05-18 22:41

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0003_alter_siteinfo_bg_col_alter_siteinfo_footer_bg_col_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='My Awesome Shop', max_length=100)),
                ('about_us', models.TextField(blank=True, help_text='Text for the footer about us section.')),
                ('phone', models.CharField(blank=True, help_text='Contact phone number.', max_length=20)),
                ('email', models.EmailField(blank=True, help_text='Contact email address.', max_length=254)),
                ('navbar_bg_color', colorfield.fields.ColorField(default='#343a40', help_text='Background color for the navigation bar. Default is Bootstrap dark (#343a40).', image_field=None, max_length=25, samples=None)),
                ('footer_bg_color', colorfield.fields.ColorField(default='#343a40', help_text='Background color for the footer. Default is Bootstrap dark (#343a40).', image_field=None, max_length=25, samples=None)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='site_logo')),
                ('image', models.ImageField(upload_to='banners')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Site Settings',
            },
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.RemoveField(
            model_name='socialmedia',
            name='footer',
        ),
        migrations.DeleteModel(
            name='SiteInfo',
        ),
        migrations.DeleteModel(
            name='SiteLogo',
        ),
        migrations.DeleteModel(
            name='Footer',
        ),
        migrations.DeleteModel(
            name='SocialMedia',
        ),
    ]
