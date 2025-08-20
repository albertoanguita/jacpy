import time
import threading


class Timer(object):
    def __init__(self, millis: int, function) -> None:
        self.millis = millis
        self.function = function
        self.alive = True
        self.t = threading.Timer(self.millis, self.function)

    def start(self) -> None:
        time.sleep(self.millis / 1000)
        if self.alive:
            self.function()

    def stop(self) -> None:
        self.alive = False