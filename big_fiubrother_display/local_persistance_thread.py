from big_fiubrother_core import StoppableThread
from os import path


class LocalPersistanceThread(StoppableThread):

    TMP_PATH = 'tmp'

    def __init__(self, configuration, input_queue, output_queue):
        super().__init__()
        self.path = configuration['tmp_path'] if 'tmp_path' in configuration else self.TMP_PATH
        self.input_queue = output_queue
        self.output_queue = output_queue
 
    def _execute(self):
        message = self.input_queue.get()

        if message is not None:
            filename = '{}_{}.h264'.format(message.camera_id, message.timestamp)
            filepath = path.join(self.path, filename)

            with open(filepath, 'wb') as file:
                file.write(message.payload)

            self.output_queue.put(filepath)

    def _stop(self):
        self.input_queue.put(None)