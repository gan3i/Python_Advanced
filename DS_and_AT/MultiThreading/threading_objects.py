import threading

sema = threading.Semaphore()

sema.acquire()
# sema.acquire()

sema.release()

def add (a,b):
    return a + b

timer = threading.Timer(2.0,add,(2,3))

timer.start()
timer.cancel()

barrier = threading.Barrier(3)