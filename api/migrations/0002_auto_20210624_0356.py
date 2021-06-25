# Generated by Django 3.2.4 on 2021-06-24 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicmodel',
            name='singer',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='title',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='musicmodel',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='videomodel',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]