from big_fiubrother_core import QueueTask
import cv2


class DisplayVideo(QueueTask):

    def __init__(self, configuration, input_queue):
        super().__init__(input_queue)
        self.window_name = configuration['name']
        self.fps = configuration['fps']
        self.frame_period = 1000 // self.fps

    def init(self):
        super().init()
        cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(
            self.window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    def execute_with(self, message):
        timestamp, frame = message
        cv2.imshow(self.window_name, frame)
        cv2.waitKey(self.frame_period)

    def stop(self):
        super().stop()
        cv2.destroyWindow(self.window_name)
