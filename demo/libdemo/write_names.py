names = ['Martin', 'Anders', 'James', 'Larry', 'Bill']

f = open("names.txt", "wt")

for name in names:
    f.write(name + "\n")

f.close()

