from django.contrib import admin
from tournament.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .forms import CreateUserForm

UserAdmin.add_form = CreateUserForm
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'email', 'birth_date', 'password1', 'password2',)
    }),
)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Tournament)
admin.site.register(Player)
admin.site.register(Scores)
