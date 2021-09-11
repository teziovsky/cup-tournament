from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from tournament.models import Tournament, Player, Scores


class TournamentsView(LoginRequiredMixin, ListView):
    model = Tournament
    login = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        now = timezone.now()
        context = super().get_context_data(**kwargs)
        context['active_tournaments'] = Tournament.objects.all().filter(start_date__gt=now)
        return context


class DetailTournamentsView(LoginRequiredMixin, DetailView):
    model = Tournament
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tournament_id = self.kwargs.get('pk')
        tournament = Tournament.objects.get(id=tournament_id)
        players = Player.objects.filter(tournament=tournament_id)
        players_length = players.count()
        scores = Scores.objects.filter(tournament=tournament_id)
        players_null_scores = Scores.objects.filter(score_player1__isnull=True).count() + Scores.objects.filter(
            score_player2__isnull=True).count()
        winner = None
        is_valid = int(tournament.max_players) == int(players_length)
        is_last_round = scores.count() == (players_length - 1)

        if is_last_round:
            last_score = scores.last()
            if last_score.score_player1 is not None and last_score.score_player2 is not None:
                if int(last_score.score_player1) > int(last_score.score_player2):
                    winner = last_score.player1
                else:
                    winner = last_score.player2

        context['players'] = players
        context['players_length'] = players_length
        context['is_valid'] = is_valid
        context['scores'] = scores
        context['winner'] = winner
        context['null_scores'] = players_null_scores
        context['is_last_round'] = is_last_round
        return context


class CreateTournamentsView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Tournament
    fields = ['name', 'start_date', 'max_players']
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('tournament_add')
    success_message = 'Tournament created successfully.'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeleteTournamentsView(LoginRequiredMixin, DeleteView):
    model = Tournament
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('tournaments')
