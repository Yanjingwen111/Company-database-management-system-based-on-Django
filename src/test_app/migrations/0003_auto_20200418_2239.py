# Generated by Django 3.0.4 on 2020-04-18 22:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_remove_casecomment_eid'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='timeframe',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customer',
            name='company',
            field=models.CharField(default='', max_length=32),
        ),
    ]
