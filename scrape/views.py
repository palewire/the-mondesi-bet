from .models import SeasonTotal
from django.http import HttpResponse


def seasontotals_latest(request):
    """
    A dump of all the latest scraped data.
    """
    obj = SeasonTotal.objects.latest()
    return HttpResponse(obj.json, content_type="application/javascript")
