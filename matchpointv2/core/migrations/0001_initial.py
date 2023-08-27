# Generated by Django 4.2.2 on 2023-07-20 18:12

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number_of_sets", models.IntegerField()),
            ],
            options={
                "verbose_name_plural": "Matches",
            },
        ),
        migrations.CreateModel(
            name="Set",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("player1_games", models.CharField(max_length=10)),
                ("player2_games", models.CharField(max_length=10)),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.match"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="match",
            name="players",
            field=models.ManyToManyField(to="core.player"),
        ),
        migrations.CreateModel(
            name="MatchStats",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "aces",
                    models.IntegerField(validators=[core.models.validate_positive]),
                ),
                (
                    "double_faults",
                    models.IntegerField(validators=[core.models.validate_positive]),
                ),
                (
                    "winners",
                    models.IntegerField(validators=[core.models.validate_positive]),
                ),
                (
                    "unforced_errors",
                    models.IntegerField(validators=[core.models.validate_positive]),
                ),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.match"
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.player"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "All Matches Statistics",
                "unique_together": {("match", "player")},
            },
        ),
    ]
