# Generated by Django 3.0.4 on 2020-03-15 04:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_auto_20200314_2304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interview',
            old_name='candiates',
            new_name='candidates',
        ),
        migrations.AlterField(
            model_name='interview',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 15, 4, 34, 51, 833465)),
        ),
        migrations.AlterField(
            model_name='interview',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 15, 4, 34, 51, 833420)),
        ),
    ]
