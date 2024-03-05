from multiprocessing import Process, Value, Array, Lock
import os
import time


def add100(number, arrays, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1
            for i in range(len(arrays)):
                arrays[i] += 1


if __name__ == '__main__':
    lock = Lock()
    shared_number = Value('i', 0)
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Number at beginning is', shared_number.value)
    print('Array at beginning is', shared_array[:])

    p1 = Process(target=add100, args=(shared_number, shared_array, lock))
    p2 = Process(target=add100, args=(shared_number, shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Number at end is', shared_number.value)
    print('Array at end is', shared_array[:])

