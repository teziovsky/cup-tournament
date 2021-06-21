from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView
from tournament.models import Tournament, Player, Scores
from random import shuffle


class UpdateScoresView(LoginRequiredMixin, UpdateView):
    model = Scores
    fields = ['score_player1', 'score_player2']
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        score_player1 = int(form.data['score_player1'])
        score_player2 = int(form.data['score_player2'])

        if score_player1 == score_player2:
            messages.error(self.request, 'Scores must be different!')
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tournament_detail', kwargs={'pk': self.kwargs.get("fk")})


def start_round(self, pk):
    Tournament.objects.filter(id=pk).update(is_started=True)
    scores = Scores.objects.filter(tournament=pk).order_by("round")

    if scores.count() == 0:
        players = Player.objects.filter(tournament=pk)
        addScores(pk, players, 1)
    else:
        last_round = scores.last().round
        scores_in_round = scores.filter(round=last_round)
        players = []
        for score in scores_in_round:
            if score.score_player1 > score.score_player2:
                players.append(score.player1)
            else:
                players.append(score.player2)

        addScores(pk, players, last_round + 1)

    return redirect('tournament_detail', pk)


def addScores(tournament_id, players, round_id):
    players = list(players)
    shuffle(players)

    for x in range(int(len(players) / 2)):
        player1 = players[0]
        player2 = players[1]
        score = Scores(tournament_id=tournament_id, player1=player1, player2=player2, round=round_id)
        score.save()
        players.remove(player1)
        players.remove(player2)
