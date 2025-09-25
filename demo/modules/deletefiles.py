
# takes directory on command-line
import sys

if len(sys.argv) < 2:
    print('Directory name is missing')
    print('python deletefiles.py  <dirname>')
    exit(1)


dirname = sys.argv[1]

print(f'Deleting files from {dirname}')