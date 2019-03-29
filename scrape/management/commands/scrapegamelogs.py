import json
import logging
import requests
import collections
from bs4 import BeautifulSoup
from django.conf import settings
from scrape.models import GameLog
from django.core.management.base import BaseCommand
logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        data = self.get_data()
        dumped = json.dumps(data, indent=4)
        obj = GameLog.objects.create(json=dumped)
        print(f"Created {obj}")

    def get_data(self):
        year_dict = collections.OrderedDict()
        for year in range(2016, 2020):
            url = f"https://www.baseball-reference.com/players/gl.fcgi?id=mondera02&t=b&year={year}"
            print(f"Requesting {url}")
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html5lib")
            table = soup.find('table', id="batting_gamelogs")
            game_list = table.find_all('tr', id=lambda x: x and x.startswith('batting_gamelogs'))
            stat_list = []
            for i, game in enumerate(game_list):
                d = collections.OrderedDict()
                d['ranker'] = game.find("th").string
                cells = game.find_all("td")
                for stat in cells:
                    if 'csk' in stat.attrs.keys():
                        d[stat['data-stat']] = stat['csk']
                    else:
                        d[stat['data-stat']] = stat.string
                stat_list.append(d)
            year_dict[year] = stat_list
        return year_dict
