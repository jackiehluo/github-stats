import requests

p = "3182"

while True:
    url = "https://api.github.com/users?since=" + p
    response = requests.get(url)
    response_dict = response.json()
    for r in response_dict:
        print r["login"], r["id"]
        if r["id"] > int(p):
            p = str(r["id"])
