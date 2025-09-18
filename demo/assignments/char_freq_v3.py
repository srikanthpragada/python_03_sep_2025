s = 'how do you do'

freq = {}
for c in s:
    if c not in freq:
        freq[c] = s.count(c)

print(freq)

