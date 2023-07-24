# Generated by Django 4.2.3 on 2023-07-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blogpost_slug_category_slug_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='header_image',
            field=models.ImageField(blank=True, height_field=500, help_text='Size = 1500px x 500px', upload_to='media/blogs/header', verbose_name='Header Image', width_field=1500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='null', max_length=75, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(blank=True, height_field=305, help_text='Size = 405px x 305px', upload_to='media/blogs/thumbs', verbose_name='Thumbnail', width_field=405),
        ),
    ]