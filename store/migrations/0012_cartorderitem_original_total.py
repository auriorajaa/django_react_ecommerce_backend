# Generated by Django 5.1.5 on 2025-01-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_cartorderitem_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorderitem',
            name='original_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
