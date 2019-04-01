from django.contrib import admin
from django.urls import path
from scrape import views


urlpatterns = [
    path('season-totals.json', views.seasontotals_latest, name="season-totals"),
    path('game-logs.json', views.gamelogs_latest, name="game-logs"),
    path('projections.json', views.projections_latest, name="projections"),
    path('admin/', admin.site.urls),
]
