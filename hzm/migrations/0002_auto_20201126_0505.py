# Generated by Django 3.1 on 2020-11-26 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hzm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='match_date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='record',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]