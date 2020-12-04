
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('club_name', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('host', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('map_name', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('date', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_name', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('passwd', models.CharField(blank=True, max_length=128, null=True)),
                ('win', models.IntegerField(blank=True, default=0, null=True)),
                ('lose', models.IntegerField(blank=True, default=0, null=True)),
                ('accept', models.BooleanField(default=False)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hzm.club')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('date_start', models.CharField(blank=True, max_length=128, null=True)),
                ('date_end', models.CharField(blank=True, max_length=128, null=True)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hzm.club')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hzm.player')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.CharField(blank=True, max_length=15, null=True)),
                ('record_date', models.CharField(blank=True, max_length=15, null=True)),
                ('match_club', models.CharField(blank=True, max_length=128, null=True)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hzm.club')),
                ('maps', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hzm.map')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hzm.player')),
            ],
        ),
        migrations.CreateModel(
            name='Post_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_blue', models.CharField(blank=True, max_length=128, null=True)),
                ('post_writer', models.CharField(blank=True, max_length=128, null=True)),
                ('passwd', models.CharField(blank=True, max_length=128, null=True)),
                ('player_num', models.IntegerField(blank=True, default=2, null=True)),
                ('red_p1_name', models.CharField(blank=True, max_length=128, null=True)),
                ('red_p2_name', models.CharField(blank=True, max_length=128, null=True)),
                ('red_p3_name', models.CharField(blank=True, max_length=128, null=True)),
                ('red_p4_name', models.CharField(blank=True, max_length=128, null=True)),
                ('red_p5_name', models.CharField(blank=True, max_length=128, null=True)),
                ('red_p6_name', models.CharField(blank=True, max_length=128, null=True)),
                ('red_p7_name', models.CharField(blank=True, max_length=128, null=True)),
                ('red_p8_name', models.CharField(blank=True, max_length=128, null=True)),
                ('blue_p1_name', models.CharField(blank=True, max_length=128, null=True)),
                ('blue_p2_name', models.CharField(blank=True, max_length=128, null=True)),
                ('blue_p3_name', models.CharField(blank=True, max_length=128, null=True)),
                ('blue_p4_name', models.CharField(blank=True, max_length=128, null=True)),
                ('blue_p5_name', models.CharField(blank=True, max_length=128, null=True)),
                ('blue_p6_name', models.CharField(blank=True, max_length=128, null=True)),
                ('blue_p7_name', models.CharField(blank=True, max_length=128, null=True)),
                ('blue_p8_name', models.CharField(blank=True, max_length=128, null=True)),
                ('match_date', models.CharField(blank=True, max_length=128, null=True)),
                ('match_time_start', models.CharField(blank=True, max_length=128, null=True)),
                ('match_time_end', models.CharField(blank=True, max_length=128, null=True)),
                ('match_map1', models.CharField(blank=True, max_length=128, null=True)),
                ('match_map2', models.CharField(blank=True, max_length=128, null=True)),
                ('match_map3', models.CharField(blank=True, max_length=128, null=True)),
                ('match_map4', models.CharField(blank=True, max_length=128, null=True)),
                ('match_map5', models.CharField(blank=True, max_length=128, null=True)),
                ('match_map6', models.CharField(blank=True, max_length=128, null=True)),
                ('match_map7', models.CharField(blank=True, max_length=128, null=True)),
                ('match_map8', models.CharField(blank=True, max_length=128, null=True)),
                ('match_map9', models.CharField(blank=True, max_length=128, null=True)),
                ('match_map10', models.CharField(blank=True, max_length=128, null=True)),
                ('match_map11', models.CharField(blank=True, max_length=128, null=True)),
                ('match_map12', models.CharField(blank=True, max_length=128, null=True)),
                ('match_map13', models.CharField(blank=True, max_length=128, null=True)),
                ('match_map14', models.CharField(blank=True, max_length=128, null=True)),
                ('date', models.CharField(blank=True, max_length=128, null=True)),
                ('red_goga_avg', models.CharField(blank=True, max_length=128, null=True)),
                ('blue_goga_avg', models.CharField(blank=True, max_length=128, null=True)),
                ('accept', models.BooleanField(default=False)),
                ('state', models.CharField(blank=True, max_length=4, null=True)),
                ('result', models.BooleanField(default=False)),
                ('blue_win', models.IntegerField(blank=True, default=0, null=True)),
                ('red_win', models.IntegerField(blank=True, default=0, null=True)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hzm.club')),
            ],
        ),
        migrations.CreateModel(
            name='Matchresult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField(default=False)),
                ('club_name', models.CharField(blank=True, max_length=128, null=True)),
                ('match', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hzm.post_list')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hzm.player')),
            ],
        ),
    ]
