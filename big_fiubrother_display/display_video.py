from big_fiubrother_core import QueueTask
import cv2


class DisplayVideo(QueueTask):

    def __init__(self, configuration, input_queue):
        super().__init__(input_queue)
        self.name = configuration['name']
        self.fps = configuration['fps']
        self.time_between_frames = 1000 // self.fps

    def init(self):
        super().init()
        cv2.namedWindow(self.name, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(
            self.name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    def execute_with(self, frame):
        cv2.imshow(self.name, frame)
        cv2.waitKey(self.time_between_frames)

    def stop(self):
        super().stop()
        cv2.destroyWindow(self.name)
