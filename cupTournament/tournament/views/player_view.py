from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView
from django.utils import timezone
from django.contrib import messages
from tournament.models import Tournament, Player


class PlayersView(LoginRequiredMixin, ListView):
    model = Player
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreatePlayersView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Player
    fields = ['name', 'tournament']
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('players')
    success_message = 'Player created successfully.'

    def form_valid(self, form):
        tournament_id = form.data['tournament']
        players_length = len(Player.objects.select_related().filter(tournament=tournament_id))
        tournament_players = int(Tournament.objects.filter(id=tournament_id).first().max_players)

        if players_length >= tournament_players:
            messages.error(
                self.request,
                "The players count can't be grater than %d" % tournament_players
            )
            return self.form_invalid(form)

        return super().form_valid(form)


class DeletePlayersView(LoginRequiredMixin, DeleteView):
    model = Player
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('players')
