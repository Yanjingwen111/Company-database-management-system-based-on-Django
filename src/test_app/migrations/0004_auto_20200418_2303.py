# Generated by Django 3.0.4 on 2020-04-18 23:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0003_auto_20200418_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='timeframe',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
