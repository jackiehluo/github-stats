from datetime import datetime
from pymongo import MongoClient
import os
import requests

from config import *


client = MongoClient()
db = client['github-stats']
#r = requests.Session()

#People who have commits from profile cheats, bots/loggers, etc.
cheaters = {"tef", "ejucovy", "kratorius", "riaf", "tanelpuhu", "will",
            "addyosmani", "Ocramius", "susheel", "mahipal", "kanzure",
            "kinlane", "weierophinney", "bapt", "avsm", "ashie", "smn"}

with open('data.txt') as f:
    for i in xrange(752154):
        f.next()
    for line in f:
        l = [w.strip() for w in line.split(":")]
        if l[0] == "User":
            user = l[1]
        elif l[0] == "Total Contributions":
            contributions = int(l[1])
        elif l[0] == "Longest Streak":
            longest_streak = int(l[1])
        elif l[0] == "Current Streak":
            current_streak = int(l[1])
            '''
            url = ("https://api.github.com/users/" + user + "?client_id=" +
                    os.environ['CLIENT_ID'] + "&client_secret=" +
                    os.environ['CLIENT_SECRET'])
            response = r.get(url)
            u = response.json()
            print u
            '''
            if user in cheaters:
                cheater = True
            else:
                cheater = False
            entry = {"username": user, 
                    "contributions": contributions,
                    "longest_streak": longest_streak,
                    "current_streak": current_streak,
                    "cheater": cheater, "last_updated": datetime.now()}
            db.users.insert(entry)
            print user