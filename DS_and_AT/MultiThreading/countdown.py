import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n > 0:
        n -=1

start = time.time()
countdown(COUNT)
end = time.time()
print('Time taken by single thread in seconds :', end - start)
thread_one = Thread(target = countdown,args = (COUNT // 2,))
thread_two = Thread(target = countdown,args = (COUNT // 2,))

start = time.time()
thread_one.start()
thread_two.start()
thread_one.join()
thread_one.join()
end = time.time()

print("Time taken by two threads in seconds : ", end - start)

