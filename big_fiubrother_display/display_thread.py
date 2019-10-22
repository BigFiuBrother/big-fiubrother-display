from big_fiubrother_core import StoppableThread
from time import time
import cv2


class DisplayThread(StoppableThread):

    def __init__(self, configuration, input_queue):
        super().__init__()
        self.name = configuration['name']
        self.fps = configuration['fps']
        self.time_between_frames = 1000 // self.fps
        self.input_queue = input_queue

        cv2.namedWindow(self.name)

    def _execute(self):
        frame = self.input_queue.get()

        if frame is not None:
            start_time = time()

            cv2.imshow(self.name, frame)

            sleep_time = np.max(self.time_between_frames - int(1000 * (time() - start_time)), 1)
            cv2.waitKey(sleep_time)

    def _stop(self):
        cv2.destroyWindow(self.name)
        self.input_queue.put(None)