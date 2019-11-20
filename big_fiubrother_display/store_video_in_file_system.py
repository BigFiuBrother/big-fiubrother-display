from big_fiubrother_core import QueueTask
from os import path


class StoreVideoInFileSystem(QueueTask):

    TMP_PATH = 'tmp'

    def __init__(self, configuration, input_queue, output_queue):
        super().__init__(input_queue)

        if 'tmp_path' in configuration:
            self.path = configuration['tmp_path']
        else:
            self.path = self.TMP_PATH

        self.output_queue = output_queue

    def execute_with(self, message):
        filepath = path.join(
            self.tmp_path, 
            '{}.mp4'.format(video_chunk.filename))

        with open(filepath, 'wb') as file:
            file.write(message.payload)

        self.output_queue.put((message.timestamp, filepath))
