# Generated by Django 5.1.5 on 2025-02-04 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_cartorder_paypal_session_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorderitem',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
