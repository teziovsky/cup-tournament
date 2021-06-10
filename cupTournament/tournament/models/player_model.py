from django.db import models
from tournament.models import Tournament
from django.urls import reverse


class Player(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=30)
    tournament = models.ForeignKey(Tournament, related_name="players", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('players_delete', kwargs={'pk': self.id})

    def __str__(self):
        return str(self.name)
