# Generated by Django 3.2.9 on 2021-12-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20211230_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]