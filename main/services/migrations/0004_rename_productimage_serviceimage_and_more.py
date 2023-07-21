# Generated by Django 4.2.3 on 2023-07-20 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_service_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImage',
            new_name='ServiceImage',
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, help_text='Slug for the service', null=True, unique=True),
        ),
        migrations.CreateModel(
            name='ServicePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Service Name')),
                ('service_badge', models.ImageField(help_text='Upload badge icon for service', upload_to='services/badge/', verbose_name='Service Badge')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Price')),
                ('currency', models.CharField(choices=[('kmr', 'KHR'), ('usd', 'USD')], default='USD', max_length=3, verbose_name='Currency')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('service', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Service', to='services.service', verbose_name='Service')),
            ],
        ),
    ]