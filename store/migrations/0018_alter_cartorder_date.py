# Generated by Django 5.1.5 on 2025-02-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_cartorderitem_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
