# Generated by Django 3.0.8 on 2020-09-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20200928_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='winner',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
