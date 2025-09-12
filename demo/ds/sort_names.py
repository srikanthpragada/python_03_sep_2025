
names = []

while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    names.append(name)

names.sort()

for name in names:
    print(name)
