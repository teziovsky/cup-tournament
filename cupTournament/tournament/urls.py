from django.urls import path
from tournament.views import *

urlpatterns = [
    path('', HistoryView.as_view(), name='history'),
    path('tournament/', TournamentsView.as_view(), name='tournaments'),
    path('tournament/add', CreateTournamentsView.as_view(), name='tournament_add'),
    path('tournament/<int:pk>', DetailTournamentsView.as_view(), name='tournament_detail'),
    path('tournament/<int:pk>/start', start_round, name='tournament_start'),
    path('tournament/<int:pk>/scores/<int:fk>/update', UpdateScoresView.as_view(), name='tournament_scores_update'),
    path('tournament/<int:pk>/delete', DeleteTournamentsView.as_view(), name='tournament_delete'),
    path('tournament/history', HistoryView.as_view(), name='history'),
    path('tournament/players', PlayersView.as_view(), name='players'),
    path('tournament/players/add', CreatePlayersView.as_view(), name='players_add'),
    path('tournament/players/<int:pk>/delete', DeletePlayersView.as_view(), name='players_delete'),
    path('tournament/login/', NewLoginView.as_view(), name='login'),
    path('tournament/logout/', NewLogoutView.as_view(), name='logout'),
    path('tournament/register/', NewRegisterView.as_view(), name='register'),
]
