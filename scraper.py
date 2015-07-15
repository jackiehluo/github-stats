from bs4 import BeautifulSoup
import requests

c = {}
ls = {}
cs = {}

for line in open('users.txt'):
    line = line.rstrip('\n')
    profile = requests.get('https://github.com/' + line)
    data = profile.text
    soup = BeautifulSoup(data)
    stats = soup.find_all("span", {"class" : "contrib-number"})
    if stats:
        contributions = int(stats[0].string.split()[0].replace(",", ""))
        longest_streak = int(stats[1].string.split()[0].replace(",", ""))
        current_streak = int(stats[2].string.split()[0].replace(",", ""))
        c[line] = contributions
        ls[line] = longest_streak
        cs[line] = longest_streak
    print "User:", line
    if stats:
        print "Total Contributions:", contributions
        print "Longest Streak:", longest_streak
        print "Current Streak:", current_streak
        print
    else:
        print

print "Top Contributions"
count = 0
for k, v in sorted(c.iteritems(), key=lambda (k, v): (v, k), reverse = True):
    count += 1
    print k, v
    if count == 10:
        break

count = 0
print "Longest Streak"
for k, v in sorted(ls.iteritems(), key=lambda (k, v): (v, k), reverse = True):
    count += 1
    print k, v
    if count == 10:
        break

count = 0
print "Longest Current Streak"
for k, v in sorted(cs.iteritems(), key=lambda (k, v): (v, k), reverse = True):
    count += 1
    print k, v
    if count == 10:
        break
