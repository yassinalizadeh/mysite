# Generated by Django 2.1.2 on 2018-10-13 15:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181013_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 13, 15, 17, 17, 789958, tzinfo=utc)),
        ),
    ]
