# Generated by Django 3.2.9 on 2021-12-29 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0002_alter_ad_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='buyer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
    ]