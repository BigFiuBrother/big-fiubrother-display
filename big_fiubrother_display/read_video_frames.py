from big_fiubrother_core import QueueTask
import cv2
import os


class ReadVideoFrames(QueueTask):

    def __init__(self, input_queue, output_queue):
        super().__init__(input_queue)
        self.input_queue = input_queue
        self.output_queue = output_queue

    def execute(self, filepath):
        cap = cv2.VideoCapture(filepath)

        while True:
            ret, frame = cap.read()

            if ret:
                self.output_queue.put(frame)
            else:
                break

        cap.release()
        os.remove(filepath)
