
names = set()  #Empty set

while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    names.add(name)


for name in sorted(names):
    print(name)
