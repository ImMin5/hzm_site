# Generated by Django 3.1 on 2020-11-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hzm', '0016_auto_20201114_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='map_test_record',
            field=models.TimeField(null=True),
        ),
    ]