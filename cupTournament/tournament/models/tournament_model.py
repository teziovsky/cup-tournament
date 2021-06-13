from django.conf import settings
from django.db import models
from django.urls import reverse

MAXPLAYER_CHOICES = (
    ('4', 4),
    ('8', 8),
    ('16', 16),
)


class Tournament(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=30)
    start_date = models.DateTimeField()
    max_players = models.CharField(default=12, choices=MAXPLAYER_CHOICES, max_length=2)
    is_started = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["start_date"]

    def get_absolute_url(self):
        return reverse('tournament_detail', kwargs={'pk': self.id})

    def __str__(self):
        return str(self.name)
