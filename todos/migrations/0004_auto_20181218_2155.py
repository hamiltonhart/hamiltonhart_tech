# Generated by Django 2.1 on 2018-12-18 21:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20181218_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='item_detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='assigned_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 18, 21, 55, 48, 538744, tzinfo=utc)),
        ),
    ]
