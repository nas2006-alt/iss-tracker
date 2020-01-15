import json

import requests
from bs4 import BeautifulSoup


class ISS:
    def __init__(self):
        self.lat = 0
        self.long = 0
        self.soup = ""
        self.location = ""
        self.json = {}

    def get_soup(self):
        link = "http://api.open-notify.org/iss-now.json"
        page = requests.get(link)
        self.soup = BeautifulSoup(page.text, 'html.parser')

    def get_json(self):
        self.json = json.loads(str(self.soup))

    def get_positon(self):
        position = self.json['iss_position']
        self.long = position['longitude']
        self.lat = position['latitude']

    def update(self):
        self.get_soup()
        self.get_json()
        self.get_positon()
