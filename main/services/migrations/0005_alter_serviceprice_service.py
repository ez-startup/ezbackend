# Generated by Django 4.2.3 on 2023-07-20 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_rename_productimage_serviceimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprice',
            name='service',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_price', to='services.service'),
        ),
    ]
