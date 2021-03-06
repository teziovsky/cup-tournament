# Generated by Django 3.2.3 on 2021-06-13 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('start_date', models.DateTimeField()),
                ('max_players', models.CharField(choices=[('4', 4), ('8', 8), ('16', 16)], default=12, max_length=2)),
                ('is_started', models.BooleanField(default=False)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('score_player1', models.PositiveIntegerField(null=True)),
                ('score_player2', models.PositiveIntegerField(null=True)),
                ('round', models.PositiveIntegerField()),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='tournament.player')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='tournament.player')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournament')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='tournament.tournament'),
        ),
    ]
