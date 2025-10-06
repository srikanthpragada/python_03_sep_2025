f = open("names.txt", "rt")

name = input("Enter name :").lower()

while True:
    line = f.readline().strip()
    if line == '': # EOF
        print('Sorry! Name not found')
        break
    if line.lower() == name:
        print('Found : ', line)
        break


f.close()



