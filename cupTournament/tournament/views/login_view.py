from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import messages
from django.urls import reverse_lazy


class NewLoginView(LoginView):
    template_name = 'tournament/login.html'

    def get_success_url(self):
        return reverse_lazy('tournaments')


class NewLogoutView(LogoutView):
    def get_next_page(self):
        return reverse_lazy('login')
