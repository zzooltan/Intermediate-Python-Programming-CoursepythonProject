from threading import Thread, Lock, current_thread
from queue import Queue # follows FIFO
import time


def worker(q, lock):
        while True:
            value = q.get()
            with lock:
                print(f'in {current_thread().name} got {value}')
            q.task_done()


if __name__ == "__main__":

    q = Queue()
    lock = Lock()
    num_threads = 10
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True # break the while loop, if it false then have to make a break in the while loop
        thread.start()

    for i in range(1, 21):
        q.put(i)
    q.join()

    print('end main')
