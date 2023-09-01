from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_positive(value):
    if value < 0:
        raise ValidationError("Value must be positive")


# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        if self.user:
            return f"{self.user.username}"
        else:
            return f"{self.name}"


class Match(models.Model):
    players = models.ManyToManyField(Player)
    number_of_sets = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.players.first()} vs {self.players.last()}"

    class Meta:
        verbose_name_plural = "Matches"


class Set(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player1_games = models.CharField(max_length=10)
    player2_games = models.CharField(max_length=10)

    def get_set_number(self) -> int:
        sets = Set.objects.filter(match=self.match)
        sets = sets.order_by("id")
        sets = list(sets)
        index = sets.index(self)

        return index + 1

    def __str__(self):
        return f"{self.match}: Set {self.get_set_number()}"


class MatchStats(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    aces = models.IntegerField(validators=[validate_positive])
    double_faults = models.IntegerField(validators=[validate_positive])
    winners = models.IntegerField(validators=[validate_positive])
    unforced_errors = models.IntegerField(validators=[validate_positive])

    class Meta:
        unique_together = ("match", "player")
        verbose_name_plural = "All Matches Statistics"

    def __str__(self):
        return f"Stats for {self.player} ({self.match})"
