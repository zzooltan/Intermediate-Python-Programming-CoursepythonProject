from threading import Lock

lock = Lock()

# -------------------------------------------
with open('Notes.txt', 'w') as file:
    file.write('some todo....')

file = open('notes.txt', 'w')
try:
    file.write('some todo.....')
finally:
    file.close()
# ------------------------------------------
lock.acquire()
# .....
lock.release()

#with lock:
    # .....

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('Exception has been handled')
#        print('exc:', exc_type, exc_val)
        print('exit')
        return True

with ManagedFile('notes.txt') as file:
    print('do some stufff...')
    file.write('Some todoo...')
    file.somemethod()
print('continuing')
