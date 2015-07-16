from bs4 import BeautifulSoup
import requests

with open('users.txt') as f:
    for i in xrange(80142):
        f.next()
    for line in f:
        line = line.rstrip('\n')
        profile = requests.get('https://github.com/' + line)
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
