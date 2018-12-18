# Generated by Django 2.1 on 2018-12-18 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='incomplete_item',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='complete_item',
            field=models.BooleanField(default=False),
        ),
    ]