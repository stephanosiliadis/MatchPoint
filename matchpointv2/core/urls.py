from django.urls import path
from .views import index, home, add, set_details

app_name = "core"
urlpatterns = [
    path("", index, name="index"),
    path("home/", home, name="home"),
    path("add/", add, name="add"),
    path("set_details/<int:match_id>/", set_details, name="set_details"),
]
