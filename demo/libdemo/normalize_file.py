import re

with open("test.txt", "rt") as f:
    contents = f.read()

new_contents = re.sub(' +', ' ', contents)

with open("test.txt", "wt") as f:
    f.write(new_contents)
