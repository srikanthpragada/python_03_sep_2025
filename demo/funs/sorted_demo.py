def convert_strip(s):
    return s.lower().strip()


names = ['Jeff', ' Andy', 'bill ', 'Larry', 'KEVIN', ' Tom ']

for n in sorted(names):
    print(n, end=' ')

print()

for n in sorted(names, key=convert_strip):
    print(n, end=' ')


for n in sorted(names, key=lambda s : s.strip().lower()):
    print(n, end=' ')


