import threading, queue,logging, time

q = queue.Queue()

def thread_function(name):
    logging.info(f"Thread {name} starting")
    time.sleep(2)
    logging.info(f"Thread {name} finishing")


def worker():
    while not q.empty():
        name = q.get()
        threading.Thread(target = thread_function,args = (name,)).start()
        q.task_done()

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

logging.info("Main  :before creating the thread")                                                                
# send 30 task requests to the worker
for item in range(30):
    q.put(item)

worker()

print("All task requests sent\n",end='')

#block until all tasks are done
q.join()
print("All work completed")
