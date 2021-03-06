# Generated by Django 3.1.4 on 2020-12-15 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hzm', '0008_auto_20201216_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='club_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='host',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='matchresult',
            name='club_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='record',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date_end',
            field=models.CharField(blank=True, max_length=19, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date_start',
            field=models.CharField(blank=True, max_length=19, null=True),
        ),
        migrations.CreateModel(
            name='Freeboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_writer', models.CharField(blank=True, max_length=12, null=True)),
                ('date', models.CharField(blank=True, max_length=10, null=True)),
                ('view', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hzm.player')),
            ],
        ),
    ]
