import json
import logging
import requests
import collections
from bs4 import BeautifulSoup
from django.conf import settings
from scrape.models import SeasonTotal
from django.core.management.base import BaseCommand
logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        data = self.get_data()
        dumped = json.dumps(data, indent=4)
        obj = SeasonTotal.objects.create(json=dumped)
        print(f"Created {obj}")

    def get_data(self):
        """
        Scrape a few Ichiro stats from baseball-reference.com.

        Returns them as an OrderedDict with season's year as the key.
        """
        # Grab HTML from baseball-reference
        url = "https://www.baseball-reference.com/players/m/mondera02.shtml"
        print(f"Requesting {url}")
        r = requests.get(url)

        # Drill down to the table with major league stats by year
        soup = BeautifulSoup(r.text, "html5lib")
        table = soup.find('table', id='batting_standard')
        year_list = table.find_all('tr', id=lambda x: x and x.startswith('batting_standard'))

        # Loop through the years...
        stat_list = []
        for i, year in enumerate(year_list):
            cells = year.find_all("td")
            d = collections.OrderedDict()
            year = year.find("th")['csk']
            d['year_ID'] = year
            for stat in cells:
                if 'csk' in stat.attrs.keys():
                    d[stat['data-stat']] = stat['csk']
                else:
                    d[stat['data-stat']] = stat.string
            stat_list.append(d)

        # Pass it back
        return stat_list
