from bs4 import BeautifulSoup
import requests

r = requests.Session()

with open('users.txt') as f:
    for count, line in enumerate(f):
        if count < 299447:
            continue
        elif count >= 299447 and count < 350000:
            line = line.rstrip('\n')
            profile = r.get('https://github.com/' + line)
            data = profile.text
            soup = BeautifulSoup(data)
            stats = soup.find_all("span", {"class" : "contrib-number"})
            if stats:
                contributions = int(stats[0].string.split()[0].replace(",", ""))
                longest_streak = int(stats[1].string.split()[0].replace(",", ""))
                current_streak = int(stats[2].string.split()[0].replace(",", ""))
                print "User:", line
                print "Total Contributions:", contributions
                print "Longest Streak:", longest_streak
                print "Current Streak:", current_streak
                print
        else:
            break
