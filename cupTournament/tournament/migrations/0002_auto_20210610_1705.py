# Generated by Django 3.2.3 on 2021-06-10 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tournament',
            options={'ordering': ['start_date']},
        ),
        migrations.AlterField(
            model_name='player',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournament', to='tournament.tournament'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='max_players',
            field=models.CharField(choices=[('4', 4), ('8', 8), ('12', 12), ('16', 16)], default=12, max_length=2),
        ),
    ]
