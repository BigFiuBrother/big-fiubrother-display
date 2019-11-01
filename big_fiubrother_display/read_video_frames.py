from big_fiubrother_core import QueueTask
import cv2
import os


class ReadVideoFrames(QueueTask):

    def __init__(self, fps, input_queue, output_queue):
        super().__init__(input_queue)
        self.frame_period = 1 / fps
        self.input_queue = input_queue
        self.output_queue = output_queue

    def execute_with(self, message):
        timestamp, filepath = message
        cap = cv2.VideoCapture(filepath)

        while True:
            ret, frame = cap.read()

            if ret:
                self.output_queue.put((timestamp, frame))
                timestamp += self.frame_period
            else:
                break

        cap.release()
        os.remove(filepath)
