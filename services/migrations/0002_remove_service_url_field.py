# Generated by Django 2.2.2 on 2019-06-19 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='url_field',
        ),
    ]
