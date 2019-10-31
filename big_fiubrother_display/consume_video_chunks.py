from big_fiubrother_core.message_clients.rabbitmq import Consumer
from big_fiubrother_core.messages import decode_message


class ConsumeVideoChunks(Task):

    def __init__(self, configuration, output_queue):
        self.consumer = Consumer(configuration, self._consumer_callback)
        self.output_queue = output_queue

    def execute(self):
        self.consumer.start()

    def stop(self):
        self.consumer.stop()

    def _consumer_callback(self, body):
        self.output_queue.put(decode_message(body))
