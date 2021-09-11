from django.db import models
from tournament.models import Tournament, Player
from django.urls import reverse


class Scores(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    player1 = models.ForeignKey(Player, related_name='player1', on_delete=models.CASCADE)
    score_player1 = models.PositiveIntegerField(null=True)
    player2 = models.ForeignKey(Player, related_name='player2', on_delete=models.CASCADE)
    score_player2 = models.PositiveIntegerField(null=True)
    round = models.PositiveIntegerField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}:{} {}'.format(self.player1, self.score_player1, self.score_player2, self.player2)

    def get_update_url(self):
        return reverse('tournament_scores_update', kwargs={'pk': self.id, 'fk': self.tournament.id})
