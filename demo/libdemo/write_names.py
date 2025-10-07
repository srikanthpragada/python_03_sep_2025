names = ['Martin', 'Anders', 'James', 'Larry', 'Bill']

with open("names.txt", "wt") as f:
    for name in names:
        f.write(name + "\n")
