from django.http import HttpResponse
from .models import SeasonTotal, GameLog


def seasontotals_latest(request):
    """
    A dump of the latest scraped season totals.
    """
    obj = SeasonTotal.objects.latest()
    return HttpResponse(obj.json, content_type="application/javascript")


def gamelogs_latest(request):
    """
    A dump of the latest scraped game logs.
    """
    obj = GameLog.objects.latest()
    return HttpResponse(obj.json, content_type="application/javascript")
