import os
import requests
from config import *

#Only included to get IDs from previously called users. Will delete after reaching ID #325781.

p = "164818"

while True:
    url = ("https://api.github.com/users?client_id=" +
            os.environ['CLIENT_ID'] + "&client_secret=" +
            os.environ['CLIENT_SECRET'] + "&since=" + p)
    response = requests.get(url)
    response_dict = response.json()
    for r in response_dict:
        print r["login"], r["id"]
        if r["id"] > int(p):
            p = str(r["id"])