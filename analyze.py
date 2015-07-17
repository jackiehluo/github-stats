c = {}
ls = {}
cs = {}
cheaters = {"tef", "ejucovy", "kratorius", "riaf", "tanelpuhu", "will",
            "addyosmani", "Ocramius", "susheel", "mahipal", "kanzure"}

with open('data.txt') as f:
    for line in f:
        l = [w.strip() for w in line.split(":")]
        if l[0] == "User":
            user = l[1]
        elif l[0] == "Total Contributions":
            c[user] = int(l[1])
            contributions = int(l[1])
        elif l[0] == "Longest Streak":
            ls[user] = int(l[1])
            longest_streak = int(l[1])
        elif l[0] == "Current Streak":
            cs[user] = int(l[1])
            current_streak = int(l[1])
            print user, contributions, longest_streak, current_streak

print "Most Contributions"
count = 0
for k, v in sorted(c.iteritems(), key=lambda (k, v): (v, k), reverse = True):
    if k not in cheaters:
        count += 1
        print k, v
    if count == 10:
        break

count = 0
print "Longest Streak"
for k, v in sorted(ls.iteritems(), key=lambda (k, v): (v, k), reverse = True):
    if k not in cheaters:
        count += 1
        print k, v
    if count == 10:
        break

count = 0
print "Longest Current Streak"
for k, v in sorted(cs.iteritems(), key=lambda (k, v): (v, k), reverse = True):
    if k not in cheaters:
        count += 1
        print k, v
    if count == 10:
        break
