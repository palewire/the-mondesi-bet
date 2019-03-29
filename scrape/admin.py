from django.contrib import admin
from scrape.models import SeasonTotal, GameLog


@admin.register(SeasonTotal)
class SeasonTotalAdmin(admin.ModelAdmin):
    pass


@admin.register(GameLog)
class GameLogAdmin(admin.ModelAdmin):
    pass
