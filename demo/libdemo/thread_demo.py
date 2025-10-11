import threading
from threading import Thread

print(threading.current_thread())
print(threading.active_count())

class ChildThread(Thread):
    def run(self):
        for n in range(1, 10):
            print(f'Child {n}', end = ' ')

ct = ChildThread()
ct.start()

for n in range(1, 10):
    print(f'Main {n}', end=' ')