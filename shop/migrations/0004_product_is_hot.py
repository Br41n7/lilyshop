# Generated by Django 5.1.4 on 2025-05-14 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_categorytranslation_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_hot',
            field=models.BooleanField(default=False),
        ),
    ]
