from big_fiubrother_core import QueueTask
from uuid import uuid4 as uuid
from os import path


class StoreVideoInFileSystem(QueueTask):

    def __init__(self, configuration, input_queue, output_queue):
        super().__init__(input_queue)
        self.output_queue = output_queue
        self.tmp_path = configuration['tmp_path']

    def execute_with(self, message):
        filepath = path.join(
            self.tmp_path, 
            '{}.mp4'.format(str(uuid())))

        with open(filepath, 'wb') as file:
            file.write(message.payload)

        self.output_queue.put((message.timestamp, filepath))
