from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView
from django.utils import timezone
from tournament.models import Player


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


class DeletePlayersView(LoginRequiredMixin, DeleteView):
    model = Player
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse('players')
