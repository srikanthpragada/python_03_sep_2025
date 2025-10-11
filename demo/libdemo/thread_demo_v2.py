import threading
from threading import Thread

print(threading.current_thread())
print(threading.active_count())

def print_numbers():
    for n in range(1, 10):
        print(f'Child {n}', end=' ')

ct = Thread(target = print_numbers)
ct.start()

for n in range(1, 10):
    print(f'Main {n}', end=' ')
