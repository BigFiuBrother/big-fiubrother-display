from big_fiubrother_core.messages import FrameMessage
from big_fiubrother_core.message_clients.rabbitmq import QueueConsumer


class FrameConsumer:

    def __init__(self, settings, output_queue):
        self.consumer = QueueConsumer(settings['host'], settings['queue'], self._consumer_callback)
        self.output_queue = output_queue
 
    def start(self):
        self.consumer.start()

    def _consumer_callback(self, body):
        self.output_queue.put(FrameMessage.decode(body))

    def stop(self):
        self.consumer.stop()