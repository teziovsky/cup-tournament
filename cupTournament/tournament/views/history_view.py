from django.views.generic import ListView
from django.utils import timezone
from tournament.models import Tournament


class HistoryView(ListView):
    model = Tournament
    template_name = 'tournament/history_list.html'

    def get_context_data(self, **kwargs):
        now = timezone.now()
        context = super().get_context_data(**kwargs)
        context['past_tournaments'] = Tournament.objects.all().filter(start_date__lt=now)
        return context
