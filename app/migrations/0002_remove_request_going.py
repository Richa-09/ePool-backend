# Generated by Django 3.0.6 on 2020-07-14 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='going',
        ),
    ]
