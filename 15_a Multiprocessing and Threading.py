from multiprocessing import Process
import os
import time


def square_numbers():
    for i in range(101):
        i * i
        time.sleep(0.1)


processes = []
num_process = os.cpu_count()

# create processes
print("Create processes")
for i in range(num_process):
    p = Process(target=square_numbers)
    processes.append(p)

# Start
print("Start processes")
for p in processes:
    if __name__ == '__main__':
        p.start()

# join
print("Join processes")
for p in processes:
    if __name__ == '__main__':
        p.join()

print('end main')

