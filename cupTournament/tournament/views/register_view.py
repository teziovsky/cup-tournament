from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from tournament.forms import CreateUserForm


class NewRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'tournament/register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    success_message = 'Account created successfully.'
