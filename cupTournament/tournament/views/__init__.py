from .tournament_view import TournamentsView, DetailTournamentsView, CreateTournamentsView, DeleteTournamentsView
from .history_view import HistoryView
from .player_view import PlayersView, CreatePlayersView, DeletePlayersView
from .login_view import NewLoginView, NewLogoutView
from .register_view import NewRegisterView
from .score_view import UpdateScoresView, start_round

__all__ = ['TournamentsView', 'DetailTournamentsView', 'CreateTournamentsView', 'DeleteTournamentsView', 'PlayersView',
           'CreatePlayersView', 'DeletePlayersView', 'HistoryView', 'NewLoginView', 'NewLogoutView', 'NewRegisterView',
           'start_round', 'UpdateScoresView']
