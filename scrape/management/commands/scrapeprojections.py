import json
import logging
import requests
import collections
from bs4 import BeautifulSoup
from django.conf import settings
from scrape.models import Projection
from django.core.management.base import BaseCommand
logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        data = self.get_data()
        dumped = json.dumps(data, indent=4)
        print(dumped)
        # obj = Projection.objects.create(json=dumped)
        # print(f"Created {obj}")

    def get_data(self):
        return {
            "steamer-update": self.get_steamer_update(),
            "thebat-ros": self.get_thebat_ros(),
            "zips-update": self.get_zips_update(),
            'depthcharts-ros': self.get_depthcharts_ros()
        }

    def get_depthcharts_ros(self):
        url = "https://www.fangraphs.com/projections.aspx?pos=all&stats=bat&type=rfangraphsdc&team=7&lg=all&players=0"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html5lib")
        table = soup.find('table', id="ProjectionBoard1_dg1_ctl00")
        for row in table.tbody.find_all("tr"):
            cell_list = row.find_all("td")
            if cell_list[0].text == "Adalberto Mondesi":
                return {
                    "hr": int(cell_list[9].string),
                    "sb": int(cell_list[15].string)
                }

    def get_zips_update(self):
        url = "https://www.fangraphs.com/projections.aspx?pos=all&stats=bat&type=uzips&team=7&lg=all&players=0"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html5lib")
        table = soup.find('table', id="ProjectionBoard1_dg1_ctl00")
        for row in table.tbody.find_all("tr"):
            cell_list = row.find_all("td")
            if cell_list[0].text == "Adalberto Mondesi":
                return {
                    "hr": int(cell_list[9].string),
                    "sb": int(cell_list[15].string)
                }

    def get_steamer_update(self):
        url = "https://www.fangraphs.com/projections.aspx?pos=all&stats=bat&type=steameru&team=7&lg=all&players=0"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html5lib")
        table = soup.find('table', id="ProjectionBoard1_dg1_ctl00")
        for row in table.tbody.find_all("tr"):
            cell_list = row.find_all("td")
            if cell_list[0].text == "Adalberto Mondesi":
                return {
                    "hr": int(cell_list[9].string),
                    "sb": int(cell_list[15].string)
                }

    def get_thebat_ros(self):
        url = "https://www.fangraphs.com/projections.aspx?pos=all&stats=bat&type=rthebat&team=7&lg=all&players=0"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html5lib")
        table = soup.find('table', id="ProjectionBoard1_dg1_ctl00")
        for row in table.tbody.find_all("tr"):
            cell_list = row.find_all("td")
            if cell_list[0].text == "Adalberto Mondesi":
                return {
                    "hr": int(cell_list[9].string),
                    "sb": int(cell_list[14].string)
                }
