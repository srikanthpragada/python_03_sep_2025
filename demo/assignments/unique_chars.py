names = ['java', 'c', 'c++', 'c#', 'python']

chars = set()
for s in names:
    chars = chars | set(s)

print(chars)