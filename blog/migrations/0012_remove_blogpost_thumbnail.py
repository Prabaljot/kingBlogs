# Generated by Django 4.2.1 on 2023-06-10 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_blogpost_thumbnail_alter_blogpost_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='thumbnail',
        ),
    ]
