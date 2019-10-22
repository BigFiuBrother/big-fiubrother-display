from big_fiubrother_core import StoppableThread
import cv2
import os


class VideoReaderThread(StoppableThread):

    def __init__(self, input_queue, output_queue):
        super().__init__()
        self.input_queue = output_queue
        self.output_queue = output_queue
 
    def _execute(self):
        filepath = self.input_queue.get()

        if filepath is not None:
            cap = cv2.VideoCapture(filepath)

            while cap.isOpened():

                ret, frame = cap.read()

                if ret:
                    self.output_queue.put(frame)

            os.remove(filepath)

    def _stop(self):
        self.input_queue.put(None)