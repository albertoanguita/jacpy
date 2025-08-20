import threading

"""ThreadSafe class defines thread safe objects. It encapsulates another 
object in a thread-safe manner."""
class ThreadSafe:
    def __init__(self, init_value):
        self.value = init_value
        self.lock = threading.Lock()

    def get(self):
        return self.value

    def set(self, value):
        with self.lock:
            self.value = value

    def get_and_set(self, value):
        with self.lock:
            old_value = self.value
            self.value = value
            return old_value