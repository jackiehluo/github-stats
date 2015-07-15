import os
import requests


users = open("users.txt", "a")
p = "161355"

while True:
    url = ("https://api.github.com/users?client_id=" +
            os.environ['CLIENT_ID'] + "&client_secret=" +
            os.environ['CLIENT_SECRET'] + "&since=" + p)
    response = requests.get(url)
    response_dict = response.json()
    for r in response_dict:
        users.write(r["login"] + "\n")
        print r["login"], r["id"]
        if r["id"] > int(p):
            p = str(r["id"])
