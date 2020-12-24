import random
import logging
from concurrent.futures import ThreadPoolExecutor
import threading


SENTINAL = object()

def producer(pipeline):
    """ pretend we are getting a message from network"""
    for index in range(10):
        message = random.randint(1, 101)
        logging.info(f"Producer got message {message}")
        pipeline.set_message(message, "Producer")

    #Send a sentinal message to tell consumer we are done
    pipeline.set_messsage(SENTINAL, "Producer")

def consumer(pipeline):
    """pretend we're saving a number in the database"""
    message = 0
    while message is not SENTINAL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINAL:
            logging.info(f"Consumer storing messages {message}")


class Pipeline:
    """
    Class to allow a single element pipeline between producer and consumer.
    """
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        logging.debug("%s:about to acquire getlock", name)
        self.consumer_lock.acquire()
        logging.debug("%s:have getlock", name)
        message = self.message
        logging.debug("%s:about to release setlock", name)
        self.producer_lock.release()
        logging.debug("%s:setlock released", name)
        return message

    def set_message(self, message, name):
        logging.debug("%s:about to acquire setlock", name)
        self.producer_lock.acquire()
        logging.debug("%s:have setlock", name)
        self.message = message
        logging.debug("%s:about to release getlock", name)
        self.consumer_lock.release()
        logging.debug("%s:getlock released", name)
    

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    # logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    with ThreadPoolExecutor(max_workers = 2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)

