# Generated by Django 3.0.6 on 2020-07-16 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_auto_20200714_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='pro',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='pro', to=settings.AUTH_USER_MODEL),
        ),
    ]
