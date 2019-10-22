from big_fiubrother_core import StoppableThread
from time import time
import cv2


class DisplayThread(StoppableThread):

    def __init__(self, configuration, input_queue):
        super().__init__()
        self.name = configuration['name']
        self.fps = configuration['fps']
        self.time_between_frames = 1000 // (self.fps * 2)
        self.input_queue = input_queue

        cv2.namedWindow(self.name)

    def _execute(self):
        frame = self.input_queue.get()

        if frame is not None:
            cv2.imshow(self.name, frame)
            cv2.waitKey(sleep_time)

    def _stop(self):
        cv2.destroyWindow(self.name)
        self.input_queue.put(None)