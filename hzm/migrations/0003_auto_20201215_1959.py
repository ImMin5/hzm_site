# Generated by Django 3.0 on 2020-12-15 10:59

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hzm', '0002_auto_20201212_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='map',
            name='map_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='passwd',
            field=models.CharField(blank=True, max_length=21, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='blue_p1_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='blue_p2_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='blue_p3_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='blue_p4_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='blue_p5_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='blue_p6_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='blue_p7_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='blue_p8_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='club_blue',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_date',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_map1',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_map10',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_map11',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_map12',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_map13',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_map14',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_map2',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_map3',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_map4',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_map5',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_map6',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_map7',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_map8',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_map9',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_time_end',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='match_time_start',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='passwd',
            field=models.CharField(blank=True, max_length=21, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='post_writer',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='red_p1_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='red_p2_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='red_p3_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='red_p4_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='red_p5_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='red_p6_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='red_p7_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='post_list',
            name='red_p8_name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='match_club',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='record_date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Matchred',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_writer', models.CharField(blank=True, max_length=12, null=True)),
                ('player_name', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=12, null=True), size=None)),
                ('player_id', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=0, null=True), size=None)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hzm.Club')),
            ],
        ),
    ]
