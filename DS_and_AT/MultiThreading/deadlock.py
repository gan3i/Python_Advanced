import threading

l = threading.Lock()

print("first lock")
l.acquire()
l.release()
print("second lock")
l.acquire()
print("this line will never get printed if the first lock is not released")
l.release()
#use lock as context manager

print("-----------------------------------------------------------------")
r_lock = threading.RLock()

print("first r_lock")
r_lock.acquire()
print("second r_lock")
r_lock.acquire()
print("threading.RLock alolows threads to acquire multiple locks we release it same number of times")
r_lock.release()
r_lock.release()