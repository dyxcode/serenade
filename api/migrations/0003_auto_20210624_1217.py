# Generated by Django 3.2.4 on 2021-06-24 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210624_0356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musicmodel',
            old_name='size',
            new_name='duration',
        ),
        migrations.RemoveField(
            model_name='imagemodel',
            name='size',
        ),
        migrations.RemoveField(
            model_name='videomodel',
            name='size',
        ),
    ]
