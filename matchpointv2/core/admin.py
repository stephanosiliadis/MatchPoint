from django.contrib import admin
from .models import Player, Match, Set, MatchStats

# Register your models here.
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Set)
admin.site.register(MatchStats)
