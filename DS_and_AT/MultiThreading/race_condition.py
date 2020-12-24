
import concurrent.futures, logging, time,threading

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
        logging.info("Thread %s: starting update", name)
        with self._lock :
            logging.debug("Lock acquired by thread {name}")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("about to release lock thread {name}")
        logging.debug("lock released  thread {name}")
        logging.info("Thread %s: finishing update", name)

if __name__ == "__main__":

    format = "%(asctime)s: %(message)s "
    logging.basicConfig(format = format, level = logging.INFO,
                        datefmt = "%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)

    database = FakeDatabase()

    logging.info(f"Testing update, starting value is {database.value}.")
    with concurrent.futures.ThreadPoolExecutor(max_workers = 2) as executor:
        for index in range(2):
            executor.submit(database.update, index)

    logging.info(f"Testing update. Ending value is {database.value}")