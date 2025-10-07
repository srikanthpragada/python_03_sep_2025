
filename = input("Enter filename :")

try:
    f = open(filename, "rt")
    contents = f.read()
    chars = len(contents)
    lines = contents.count('\n')
    words = contents.count(' ') + lines
    print(f'Chars  : {chars:3}')
    print(f'Words  : {words:3}')
    print(f'Lines  : {lines:3}')
    f.close()
except Exception  as ex:
    print('Error : ', ex)

