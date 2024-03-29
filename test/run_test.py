#!/usr/bin/python3

from big_fiubrother_core.messages import VideoChunkMessage
from big_fiubrother_core.message_clients.rabbitmq import Publisher
from glob import glob


class VideoChunkPublisher:

    def __init__(self, configuration):
        self.publisher = Publisher(configuration)
        self.index = 0.0

    def publish(self, video_chunk_path):
        with open(video_chunk_path, 'rb') as file:
            buffer = file.read()

        message = VideoChunkMessage(camera_id='TEST_CAMERA',
                                    timestamp=self.index,
                                    payload=buffer)

        self.publisher.publish(message)
        
        print(self.index)
        self.index += 1.0

        return message

configuration = {
  'host': 'localhost',
  'username': 'fiubrother',
  'password': 'alwayswatching',
  'exchange': 'fiubrother',
  'routing_key': 'frames'
}

publisher = VideoChunkPublisher(configuration)

for filepath in sorted(glob('../tmp/*')):
  publisher.publish(filepath)