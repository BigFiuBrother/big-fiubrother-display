from big_fiubrother_core import StoppableThread
from datetime import datetime
import cv2


class DisplayThread(StoppableThread):

    def __init__(self, configuration, input_queue):
        super().__init__()
        self.name = configuration['name']
        self.fps = configuration['fps']
        self.time_between_frames = 1000 // self.fps
        self.input_queue = input_queue

        cv2.namedWindow(self.name, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(self.name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);

    def _execute(self):
        frame = self.input_queue.get()

        if frame is not None:
            print(datetime.now())
            cv2.imshow(self.name, frame)
            cv2.waitKey(self.time_between_frames)

    def _stop(self):
        cv2.destroyWindow(self.name)
        self.input_queue.put(None)