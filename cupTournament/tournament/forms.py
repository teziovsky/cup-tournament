from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    birth_date = forms.DateField(input_formats=['%d-%m-%Y'],
                                 help_text="Field is required. Valid format of date is DD-MM-YYYY.", required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[
            'password1'].help_text = "Password can't be too similar to personal information, be a commonly used password and contain at least 8 characters"
        self.fields['password2'].label = "Password confirm"

    class Meta:
        model = User
        fields = ['username', 'email', 'birth_date', 'password1', 'password2']
        help_texts = {
            'username': 'Field is required.',
            'email': 'Field is required. Must be a valid email address.',
        }

    def save(self, commit=True):
        user = super(CreateUserForm, self).save()
        user.birth_date = self.cleaned_data['birth_date']
        if commit:
            user.save()
        return user
