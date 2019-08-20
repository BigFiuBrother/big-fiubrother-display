from time import sleep
from threading import Thread
import cv2

class DisplayThread:

    def __init__(self, input_queue, fps):
        self.fps = fps
        self.sleep_time = 1 / self.fps
        self.input_queue = input_queue

        self.running = False
        self._thread = Thread(target=self._run)

    def start(self):
        self.running = True
        self._thread.start()

    def _run(self):
        while self.running:
            sleep(self._sleep_time)

    def stop(self, wait=False):
        self.running = False

        if wait:
            self.wait_until_stopped()

    def wait_until_stopped(self): 
        self._thread.join()
