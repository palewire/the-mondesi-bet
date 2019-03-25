from django.contrib import admin
from scrape.models import SeasonTotal


@admin.register(SeasonTotal)
class SeasonTotalAdmin(admin.ModelAdmin):
    pass
