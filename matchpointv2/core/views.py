from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Player, Match, Set


# Create your views here.
def index(request):
    return render(request, "core/index.html")


def home(request):
    if not request.user.is_authenticated:
        return redirect(reverse("users:login"))

    # Filter matches and get all that contain request.user as a player
    matches = Match.objects.filter(players__user=request.user)

    return render(
        request,
        "core/home.html",
        {
            "active_nav": "home",
            "matches": matches,
        },
    )


def add(request):
    if request.method == "POST":
        name = request.POST["opponent"]
        opponent = Player(name=name)
        opponent.save()
        number_of_sets = request.POST["num-sets"]
        match = Match(number_of_sets=number_of_sets)
        match.save()
        match.players.add(opponent, request.user.player)

        return redirect(reverse("core:set_details", args=[match.id]))

    return render(
        request,
        "core/add.html",
        {
            "active_nav": "add",
        },
    )


def set_details(request, match_id):
    match = Match.objects.get(id=match_id)
    num_sets = match.number_of_sets

    if request.method == "POST":
        user_games = request.POST.getlist("user-games")
        opponent_games = request.POST.getlist("opponent-games")

        for user_game, opponent_game in zip(user_games, opponent_games):
            set = Set(match=match, player1_games=user_game, player2_games=opponent_game)
            set.save()

        return redirect(reverse("core:home"))

    return render(
        request,
        "core/set_details.html",
        {
            "active_nav": "add",
            "num_sets": num_sets,
            "match_id": match_id,
        },
    )


def match_statistics(request, match_id):
    match = Match.objects.get(id=match_id)

    return render(
        request,
        "core/match_statistics.html",
        {},
    )
