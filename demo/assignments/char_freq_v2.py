s = 'how do you do'

found = []
for c in s:
    if c not in found:
        print(c, s.count(c))
        found.append(c)

