# Generated by Django 3.0.4 on 2020-03-15 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_auto_20200315_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 15, 11, 45, 0, 562849)),
        ),
        migrations.AlterField(
            model_name='interview',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 15, 11, 45, 0, 562808)),
        ),
    ]
