import re

filename = "story.txt"

with open(filename, 'rt') as f:
    contents = f.read()

words = re.findall(r'\w+', contents)

for word in sorted(set(words)):
    print(word, end=' ')
