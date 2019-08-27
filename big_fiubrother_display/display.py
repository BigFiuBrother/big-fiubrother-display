from big_fiubrother_core import StoppableThread
from big_fiubrother_core.image_processing_helper import bytes_to_image, image_to_RGB
import matplotlib.pyplot as plt
from time import time, sleep


class Display(StoppableThread):

    def __init__(self, fps, input_queue):
        super().__init__()
        self.fps = fps
        self.time_between_frames = 1 / self.fps
        
        self.input_queue = input_queue
        
        plt.axis('off')

    def stop(self):
        plt.close()
        super().stop()

    def _execute(self):
        frame_message = input_queue.get()

        start_time = time()

        plt.imshow(_frame_to_image(frame_message.frame))
        plt.show(block=False)

        sleep_time = np.max(self.time_between_frames - (time() - start_time), 0)
        sleep(sleep_time)

    def _frame_to_image(self,frame):
        return image_to_RGB(bytes_to_image(frame_message))
