from big_fiubrother_core import StoppableThread
from time import sleep
import cv2


class DisplayThread(StoppableThread):

    def __init__(self, fps, input_queue):
        super().__init__()
        self.fps = fps
        self.sleep_time = 1 / self.fps
        
        self.input_queue = input_queue

    def _execute(self):
        frame = input_queue.get()
        #TODO: Display frame in opencv fashion
        sleep(sleep_time)
