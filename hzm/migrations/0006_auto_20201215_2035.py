# Generated by Django 3.0 on 2020-12-15 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hzm', '0005_auto_20201215_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='club_blue_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='club_red_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]