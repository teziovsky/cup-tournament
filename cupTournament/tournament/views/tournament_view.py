from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from tournament.models import Tournament, Player
import random


class TournamentsView(ListView):
    model = Tournament

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
        context['now'] = timezone.now()
        players = Player.objects.select_related().filter(tournament=kwargs['object'])
        players_length = players.count
        context['players'] = players
        context['players_length'] = players_length
        return context


class CreateTournamentsView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Tournament
    fields = ['name', 'start_date', 'max_players']
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('tournaments')


class DeleteTournamentsView(LoginRequiredMixin, DeleteView):
    model = Tournament
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('tournaments')
