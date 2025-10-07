
filename = input("Enter filename :")

try:
    f = open(filename, "rt")
    search_string = input("Enter search string :")

    for lineno, line in enumerate(f.readlines(), start = 1):
        if search_string in line:
            print(f'Found at {lineno}')
            break
    else:
        print('Sorry! Not found!')

    f.close()
except Exception  as ex:
    print('Error : ', ex)

