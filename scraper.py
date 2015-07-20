from bs4 import BeautifulSoup
from datetime import datetime
from pymongo import MongoClient
import os
import requests

from config import *


client = MongoClient()
db = client['github-stats']
r = requests.Session()
p = "406853"

while True:
    url = ("https://api.github.com/users?client_id=" +
            os.environ['CLIENT_ID'] + "&client_secret=" +
            os.environ['CLIENT_SECRET'] + "&since=" + p)
    response = r.get(url)
    users = response.json()
    for user in users:
        profile = r.get('https://github.com/' + user["login"])
        soup = BeautifulSoup(profile.text)
        stats = soup.find_all("span", {"class" : "contrib-number"})
        if stats:
            contributions = int(stats[0].string.split()[0].replace(",", ""))
            longest_streak = int(stats[1].string.split()[0].replace(",", ""))
            current_streak = int(stats[2].string.split()[0].replace(",", ""))
            entry = {"id": user["id"],
                    "username": user["login"],
                    "contributions": contributions,
                    "longest_streak": longest_streak,
                    "current_streak": current_streak,
                    "last_updated": datetime.now()}
            db.users.insert(entry)
            print user["login"], user["id"]
        if user["id"] > int(p):
            p = str(user["id"])