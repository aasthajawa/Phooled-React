# Generated by Django 5.0.2 on 2024-03-23 05:23

import django.db.models.deletion
import django.utils.timezone
import django_fsm
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_remove_gameroom_game_started_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhishGameSession',
            fields=[
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefg1234', length=16, max_length=40, prefix='id_', primary_key=True, serialize=False)),
                ('owner', models.IntegerField(default=0)),
                ('turn', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('num_cards', models.IntegerField(default=15)),
                ('qf_time_limit', models.IntegerField(default=60)),
                ('ar_time_limit', models.IntegerField(default=60)),
                ('fr_time_limit', models.IntegerField(default=30)),
            ],
            options={
                'verbose_name': 'PhishGame Session',
                'verbose_name_plural': 'PhishGame Sessions',
                'db_table': 'phishgame_game_session',
            },
        ),
        migrations.CreateModel(
            name='GameState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('state', models.CharField(choices=[('idle', 'idle'), ('game_proposal', 'game_proposal'), ('game_settings', 'game_settings'), ('set_up_qf_distribute_cards', 'set_up_qf_distribute_cards'), ('set_up_qf_ready_up', 'set_up_qf_ready_up'), ('qf_tear_down', 'qf_tear_down'), ('qf', 'qf'), ('set_up_ar', 'set_up_ar'), ('ar', 'ar'), ('set_up_fr', 'set_up_fr'), ('fr_init', 'fr_init'), ('fr_classify_init', 'fr_classify_init'), ('fr_classify', 'fr_classify'), ('fr_classify_tear_down', 'fr_classify_tear_down'), ('fr_classify_result', 'fr_classify_result'), ('fr_init_attr', 'fr_init_attr'), ('fr_attr_solo', 'fr_attr_solo'), ('fr_attr_group', 'fr_attr_group'), ('fr_attr_tear_down', 'fr_attr_tear_down'), ('fr_attr_result', 'fr_attr_result'), ('fr_result', 'fr_result'), ('fr_wild', 'fr_wild'), ('finish', 'finish')], default='idle', max_length=30)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.phishgamesession')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, django_fsm.FSMFieldMixin),
        ),
    ]
