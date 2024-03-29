# Generated by Django 4.2.3 on 2023-07-20 04:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_line', models.CharField(choices=[('mobile', 'Mobile'), ('home', 'Home'), ('work', 'Work'), ('emergency', 'Emergency')], default='Mobile', max_length=25, verbose_name='Name')),
                ('phone_number', models.IntegerField(default='Mobile', max_length=15, verbose_name='Phone Number')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]
