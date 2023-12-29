from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Player, Match, Set, MatchStats


# Create your views here.
def index(request):
    return render(request, "core/index.html")


def home(request):
    if not request.user.is_authenticated:
        return redirect(reverse("users:login"))

    # Filter matches and get all that contain request.user as a player
    matches = Match.objects.filter(players__user=request.user)

    # Calculate total games won by each player
    for match in matches:
        players = list(match.players.all())
        for i, player in enumerate(players):
            total_games = 0
            for set in match.set_set.all():
                if player == match.players.first():
                    total_games += int(set.player1_games)
                else:
                    total_games += int(set.player2_games)
            player.total_games = total_games
            # Determine the winner
            other_player = players[1 - i]
            if "total_games" in other_player.__dict__:
                if player.total_games > other_player.total_games:
                    player.is_winner = True
                else:
                    player.is_winner = False

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

        return redirect(reverse("core:match_stats", args=[match.id]))

    return render(
        request,
        "core/set_details.html",
        {
            "active_nav": "add",
            "num_sets": num_sets,
            "match_id": match_id,
        },
    )


def match_stats(request, match_id):
    match = Match.objects.get(id=match_id)
    user = Player.objects.get(user=request.user)
    opponent = match.players.exclude(user=request.user).first()

    if request.method == "POST":
        user_data = {
            k.replace("user-", ""): v
            for k, v in request.POST.items()
            if k.startswith("user-")
        }
        opponent_data = {
            k.replace("opponent-", ""): v
            for k, v in request.POST.items()
            if k.startswith("opponent-")
        }

        user_stats = MatchStats(match=match, player=user, **user_data)
        opponent_stats = MatchStats(match=match, player=opponent, **opponent_data)

        user_stats.save()
        opponent_stats.save()

        print(user_stats, opponent_stats)

        # Redirect to home if form inputs are valid
        return redirect(reverse("core:home"))

    return render(
        request,
        "core/match_statistics.html",
        {
            "active_nav": "add",
            "match_id": match_id,
        },
    )
